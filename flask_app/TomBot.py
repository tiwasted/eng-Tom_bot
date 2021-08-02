import telebot
import schedule
import time
import sqlite3 as sql
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Добро пожаловать мой дорогой друг, начнем обучение")


@bot.message_handler(commands=['learn'])
def send_m(message):
    if message.chat.id in config.admin:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            con.commit()

            for value in cur.execute("SELECT engg FROM words ORDER BY RANDOM() LIMIT 1"):
                msg = bot.send_message(message.chat.id, value)
                bot.register_next_step_handler(msg, process_rus_step)


def process_rus_step(message):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        con.commit()
        rus_w = message.text.lower()
        msg = rus_w
        cur.execute(f"SELECT russ FROM words WHERE russ = '{msg}'")
        if cur.fetchone() is None:
            bot.reply_to(message, "Надо бы тебе ещё поучить")
        else:
            bot.reply_to(message, "Верно!")

    schedule.every(30).minutes.do(lambda: send_m(message))

    while True:
        schedule.run_pending()
        time.sleep(1)


bot.polling()
