from pyrogram import Client, filters
import time

app = Client('Glut drochilna')

def drochit(chat, msg, zd):
    print('Окей! Все готово! Дрочилка началась')
    while True:
        app.send_message(chat, msg)
        time.sleep(int(zd))
        
@app.on_message()
def cum(client, message):
    global chat
    if message.text == 'этот':
        chat = message.chat.id
        chekin()
    elif message.text == 'Этот':
        chat = message.chat.id
        chekin()
        
print('Привет! Это тг автодрочер')
chat = input('Введи айди чата (оставь пустым если хочешь выбрать его командой): ')
msg = input('Введи сообщение: ')
zd = input('Введи задержку в секундах: ')

def chekin():
    global msg
    global zd
    if bool(chat) == False:
        print('Окей, введи в любой нужный тебе чат слово ''этот'' и я сам заполню переменную')

    if bool(msg) == False:
        print('Аче отсылать тогда, ты это, лучше напиши')
        msg = input('Введи сообщение: ')

    if bool(zd) == False:
        print('Акакая задержка, ты это, лучше напиши')
        zd = input('Введи задержку: ')
    
    if bool(chat) == True:
        drochit(chat, msg, zd)

chekin()




app.run()