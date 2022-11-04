import os
from aiogram import Bot, Dispatcher, executor, types
import sqlite3
from aiogram.types import ContentType, InlineKeyboardButton, InlineKeyboardMarkup, Message, callback_query
import time
from config import *


bot = Bot(token=bot_t)
dp = Dispatcher(bot)
chat_id = -1001814953183


@dp.message_handler(commands=['users'], commands_prefix='/')
async def rrrr(message: types.Message):
    db = sqlite3.connect('list.db')
    sql = db.cursor()
    data = sql.fetchone()
    d = message.from_user.id
    sql.execute(f"SELECT id FROM w_gfff WHERE id = '{d}'")
    db.commit()

    if sql.fetchone():
        t = InlineKeyboardButton(text='Список клиентов')
        r = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Вывести список', callback_data='f'))
        await message.answer('Список клиентов', reply_markup=r)
@dp.callback_query_handler(text='f')
async def yyy(callback : types.CallbackQuery):
    sqlite_connection = sqlite3.connect('list.db')
    cursor = sqlite_connection.cursor()

    sqlite_select_query = """SELECT * from w_gf"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    for row in records:
        for value in sqlite_connection.execute(f"SELECT comp FROM w_gf WHERE id = '{row[0]}'"):

            s1 = str(value)
            f = str(s1[2:-3])
            ef = str(row[1])
            h = (f'{ef}')
            a = str(row[0])
            r = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text=a, switch_inline_query_current_chat=row[0]))

            await bot.send_message(chat_id, h, reply_markup=r)


@dp.message_handler(commands=['start'], commands_prefix='/')
async def rr(message: types.Message):
    db = sqlite3.connect('list.db')
    sql = db.cursor()
    data = sql.fetchone()
    d = message.from_user.id
    sql.execute(f"SELECT id FROM w_gf WHERE id = '{d}'")
    db.commit()

    if sql.fetchone():
        await bot.send_message(message.from_user.id, "Здравствуйте, Вас приветствует бухгалтерский отдел компании «LQ ALLIANCE». Мы рады видеть вас в числе наших постоянных клиентов и готовы начать сотрудничество в бухгалтерском и юридическом сопровождении.\n\nКонтактные данные:\n📞 +998(98) 188-18-98\n📞 +998(91) 015-55-11\n\nС уважением, компания «LQ ALLIANCE»")


    else:
        await bot.send_message(message.chat.id, "Для получения доступа пожалуйста, обращайтесь по нижеперечисленными контактами: \n\nКонтактные данные:\n📞 +998(98) 188-18-98 \n📞 +998(91) 015-55-11\n\nС уважением, компания «LQ ALLIANCE»")
@dp.message_handler(content_types=ContentType.PHOTO)
async def p(message: Message):
    db = sqlite3.connect('list.db')
    sql = db.cursor()
    data = sql.fetchone()
    d = message.from_user.id
    sql.execute(f"SELECT id FROM w_gf WHERE id = '{d}'")
    db.commit()
    if sql.fetchone():
        s = time.time()
        f = time.ctime(s)
        r = f[11:13]
        d = int(r)
        w = f.lower()
        if 9 > d > 18 or 'sun' in w or 'sat' in w:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')
                await bot.send_photo(chat_id, message.photo[-1].file_id, f"ID:{message.chat.id} \n{h} \n {message.caption} ", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,'Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00С уважением команда компании LQ ALLIANCE')

        else:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')
                await bot.send_photo(chat_id, message.photo[-1].file_id, f"ID:{message.chat.id} \n{h} \n {message.caption} ", parse_mode='MARKDOWN')

    else:
        if message.reply_to_message:
            if message.reply_to_message.from_user.id == 5761735398:
                d = (message.reply_to_message.text)
                f = message.reply_to_message.text
                k = f[3:13]
                await bot.send_message(chat_id, text=f"ID:{k}  \n \n{message.text}",
                                       parse_mode='MARKDOWN')
                await bot.send_photo(d[3:13], message.photo[-1].file_id)

            else:
                return
@dp.message_handler(content_types=ContentType.VOICE)
async def p(message: Message):
    db = sqlite3.connect('list.db')
    sql = db.cursor()
    data = sql.fetchone()
    d = message.from_user.id
    sql.execute(f"SELECT id FROM w_gf WHERE id = '{d}'")
    db.commit()
    if sql.fetchone():
        s = time.time()
        f = time.ctime(s)
        r = f[11:13]
        d = int(r)
        w = f.lower()
        if 9 > d > 18 or 'sun' in w or 'sat' in w:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')
                await bot.send_voice(chat_id, message.voice.file_id, f"ID:{message.chat.id} \n{h} ", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,'Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00С уважением команда компании LQ ALLIANCE')

        else:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')
                await bot.send_voice(chat_id, message.voice.file_id, f"ID:{message.chat.id} \n{h} ", parse_mode='MARKDOWN')

    else:
        if message.reply_to_message:
            if message.reply_to_message.from_user.id == 5761735398:
                d = (message.reply_to_message.text)
                f = message.reply_to_message.text
                k = f[3:13]
                await bot.send_message(chat_id, text=f"ID:{k}  \n \n{message.text}",
                                       parse_mode='MARKDOWN')
                await bot.send_voice(d[3:13], message.voice.file_id)

            else:
                return
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def p(message: Message):
    db = sqlite3.connect('list.db')
    sql = db.cursor()
    data = sql.fetchone()
    d = message.from_user.id
    sql.execute(f"SELECT id FROM w_gf WHERE id = '{d}'")
    db.commit()
    if sql.fetchone():
        s = time.time()
        f = time.ctime(s)
        r = f[11:13]
        d = int(r)
        w = f.lower()
        if 9 > d > 18 or 'sun' in w or 'sat' in w:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')
                await bot.send_document(chat_id, message.document.file_id, caption=f"ID:{message.chat.id} \n{h} \n {message.caption} ", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,
                               'Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00С уважением команда компании LQ ALLIANCE')

        else:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')
                await bot.send_document(chat_id, message.document, caption=f"ID:{message.chat.id} \n{h} \n {message.caption} ", parse_mode='MARKDOWN')
    else:
        if message.reply_to_message:
            if message.reply_to_message.from_user.id == 5761735398:
                d = (message.reply_to_message.text)
                f = message.reply_to_message.text
                k = f[3:13]
                await bot.send_message(chat_id, text=f"ID:{k}  \n \n{message.text}",
                                       parse_mode='MARKDOWN')
                await bot.send_document(d[3:13], message.document.file_id)

            else:
                return
@dp.message_handler()
async def h(message: types.Message):
    db = sqlite3.connect('list.db')
    sql = db.cursor()
    data = sql.fetchone()
    d = message.chat.id
    sql.execute(f"SELECT id FROM w_gf WHERE id = '{d}'")
    db.commit()

    if sql.fetchone():
        s = time.time()
        f = time.ctime(s)
        r = f[11:13]
        d = int(r)
        w = f.lower()
        if 8 > d > 17 or 'sun' in w or 'sat' in w:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')

                await bot.send_message(chat_id, text=f"ID:{message.chat.id} \n {h} \n {message.text.message_id}  \n \n{message.text}", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,
                                       f'{message.message_id}Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00С уважением команда компании LQ ALLIANCE')

        else:
            for value in sql.execute(f"SELECT comp FROM w_gf WHERE id = '{message.chat.id}'"):
                d = '*{0.first_name}*'.format(message.from_user)
                s1 = str(value)
                f = str(s1[2:-3])
                h = (f'*{f}*')

                await bot.send_message(chat_id,
                                       text=f"ID:{message.chat.id} \nmsg_id{h}, \n {message.message_id}  \n \n{message.text}",
                                       parse_mode='MARKDOWN')


    else:
        if message.reply_to_message:

            if message.reply_to_message.from_user.id == 5761735398:
                if message.text == "20":

                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено в течении 20 минут.')
                if message.text == "40":

                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено в течении 40 минут.')
                if message.text == "60":

                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await bot.send_message(d[3:13],' Уважаемый клиент, ваше поручение будет выполнено в течении часа.')
                if message.text == '1 день':

                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено завтра в течении рабочего дня.')
                if message.text == '2 дня':
                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await bot.send_message(d[3:13],
                                           'Уважаемый клиент, ваше поручение будет выполнено в течении 2-х рабочих дней.')
                if message.text == '3 дня':

                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено в течении 3-х рабочих дней.')
                if not message.text == "20" and not message.text == "40" and not message.text == "60" and not message.text == "1 день" and not message.text == "2 дня" and not message.text == "3 дня" :
                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]

                    await  bot.send_message(d[3:13], message.text)
            else:
                db = sqlite3.connect('list.db')
                sql = db.cursor()
                data = sql.fetchone()
                d = message.from_user.id

                inp_str = message.reply_to_message.text
                num = ""
                for c in inp_str:
                    if c.isdigit():
                        num = num + c
                sql.execute(f"SELECT id FROM w_gf WHERE id = '{num}'")
                db.commit()

                if sql.fetchone():
                    if message.text == "20":

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено в течении 20 минут.')
                    if message.text == "40":

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено в течении 40 минут.')
                    if message.text == "60":

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num,' Уважаемый клиент, ваше поручение будет выполнено в течении часа.')
                    if message.text == '1 день':

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено завтра в течении рабочего дня.')
                    if message.text == '2 дня':
                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num,
                                           'Уважаемый клиент, ваше поручение будет выполнено в течении 2-х рабочих дней.')
                    if message.text == '3 дня':

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено в течении 3-х рабочих дней.')
                    if not message.text == "20" and not message.text == "40" and not message.text == "60" and not message.text == "1 день" and not message.text == "2 дня" and not message.text == "3 дня" :
                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(num, message.text)
        else:
                    return



executor.start_polling(dp, skip_updates=True)