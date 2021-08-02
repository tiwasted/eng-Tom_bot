from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('f_in_words.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            eng = request.form['english']
            rus = request.form['russian']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO words (engg, russ) VALUES(?, ?)", (eng, rus))

                con.commit()
                msg = "Слова успешно добавленны"
        except:
            con.rollback()
            msg = "Ошибка"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


if __name__ == '__main__':
    app.run(debug=True)
