import sqlite3
import sqlite3

bot = st.TeleBot('7481783584:AAH41qhOYWjvoD4V6xFYldizVXAfqiyANAY')

user = bot.get_me()  
userid = user.id

#sqlite setup
conn = sqlite3.connect('database.sql')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id int  primary key, rep int)')
cur.execute('INSERT INTO users (id) VALUES (?), (7481783584)')
conn.commit()
conn.close()




from random import choice
saytxt = ['Мяу', 'Мур', 'Мр-р', 'Мя-а-а', 'Мяф', 'Ме', 'Иди на Дром']

@bot.message_handler(commands=['pet'])
def pet(message):
    bot.send_message(message.chat.id, 'Мурчит')
    bot.send_message(message.chat.id, 'Вы погладили Белочку')
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int  primary key, rep int)')
    cur.execute('INSERT INTO users (rep) VALUES (?)', (152))
    conn.commit()
    conn.close()
    


@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, '*Тыгдык-тыгдык*')
    bot.send_message(message.chat.id, '*Прыг*')
    bot.send_message(message.chat.id, '*Тыгдык-тыгдык*')
    bot.send_message(message.chat.id, '*Кусь*')
    bot.send_message(message.chat.id, 'Вы поиграли с Белочкой')

@bot.message_handler(commands=['feed'])
def feed(message):
    bot.send_message(message.chat.id, '*Кушает*')
    bot.send_message(message.chat.id, 'Вы покормили Белочку')

@bot.message_handler(commands=['say'])
def say(message):
    bot.send_message(message.chat.id, choice(saytxt))

@bot.message_handler(commands=['rep'])
def rep(message):
    bot.send_message(message.chat.id, 'WIP')
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int primary key, rep int)')
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    for rep in users:
        print(rep)
        bot.send_message(message.chat.id, (rep))
    conn.commit()
    conn.close()
    

@bot.message_handler(commands=['devtokenAH78BLKNM1272J0510'])
def devtoken(message):
    bot.send_message(message.chat.id, 'DevToken accepted')

@bot.message_handler(commands=['redeem HJK89L'])
def redeemHJK89L(message):
    bot.send_message(message.chat.id, 'Вы активировали промокод')
    bot.send_message(message.chat.id, 'Вам выдан статус VIP на неделю')

@bot.message_handler(commands=['ударить', 'пнуть', 'hit', 'kick'])
def hitHUD(message):
    bot.send_message(message.chat.id, 'МЯФК')
    bot.send_message(message.chat.id, '*шипит*')
    bot.send_message(message.chat.id, 'Вы ударили Белочку')
    bot.send_message(message.chat.id, '(Как вы могли)')

@bot.message_handler(commands=['ver'])
def ver(message):
    bot.send_message(message.chat.id, 'current version is 0.2')
    bot.send_message(message.chat.id, 'to see changelog type /changelog')

@bot.message_handler(commands=['changelog', 'clog'])
def clog(message):
    bot.send_message(message.chat.id, 'added /ver, /changelog, /hit, /redeem')

@bot.message_handler(commands=['mid'])
def clog(message):
    bot.send_message(message.chat.id, userid)

bot.polling(none_stop=True)