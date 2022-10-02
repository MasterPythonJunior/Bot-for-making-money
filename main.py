import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.utils import executor
from dotenv import load_dotenv
from config import *
from keyboards import *
from db import *

load_dotenv()

BOT_NAME = os.getenv('BOT_NAME')
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    if message.chat.type == 'private':
        try:
            if select_banned_id(message.from_user.id):
                await message.answer('Вы забанены и не можете управлять ботом')

        except:
            try:
                add_users(message.from_user.id, message.from_user.first_name)
            except:
                pass
            if not user_exists(message.from_user.id):
                start_command = message.text
                referrer_id = str(start_command[7:])
                if str(referrer_id):
                    if str(referrer_id) != str(message.from_user.id):
                        add_user_ref(message.from_user.id, referrer_id)
                        try:
                            await bot.send_message(referrer_id,
                                                   'По ващей ссылке зарегистрировался новый пользователь')
                            sum = int(select_balance(referrer_id)) + 5
                            add_money(sum, referrer_id)
                        except:
                            pass
                    else:
                        await bot.send_message(message.from_user.id, 'Нельзя регистрироваться по своей же ссылке')
                else:
                    try:
                        add_user(message.from_user.id)
                    except:
                        pass
            await message.answer("""
                    Добро Пожаловать в Buffalo! 🔥
                    
                    💵Buffalo - Это легендарный-бот по заработку 🤑, вы получаете Рубли за обычные действия!
                    Нажми на кнопку "Выполнить Задание" и начни получать деньги 💵!
                    
                    
                    👨‍💻Тех.Поддержка - /support
                    ❓Помощь - /help
                        """, reply_markup=main())


@dp.message_handler(commands=['add_channel'])
async def add_channel_in_base(message: Message):
    price = message.text.split(' ')[1]
    link = message.text.split(' ')[2]
    time = message.text.split(' ')[3]
    url = message.text.split(' ')[4]
    insert_channel(price, link, time, url)
    CHANNEL_LINKS['channels'].append(link)


@dp.message_handler(commands=['add_site'])
async def add_link_in_base(message: Message):
    price = message.text.split(' ')[1]
    link = message.text.split(' ')[2]
    time = message.text.split(' ')[3]
    insert_site(price, link, time)
    CHANNEL_LINKS['links'].append(link)


@dp.message_handler(commands=['delete_channel'])
async def delete_channel_in_base(message: Message):
    link = message.text.split(' ')[1]
    delete_channel(link)
    CHANNEL_LINKS['channels'].remove(link)


@dp.message_handler(commands=['delete_link'])
async def delete_link_in_base(message: Message):
    link = message.text.split(' ')[1]
    delete_site(link)
    CHANNEL_LINKS['links'].remove(link)


@dp.message_handler(commands=['send_all'], user_id=['631357872', '710258253'])
async def sendall(message: Message):
    if message.chat.type == 'private':
        text = message.text[9:]
        users = get_users()
        for row in users:
            await bot.send_message(row[0], text)


@dp.message_handler(commands=['get'])
async def get(message: Message):
    chat_id = message.chat.id
    money = message.text.split(' ')[1]
    balance = select_balance(chat_id)
    try:
        link = message.text.split(' ')[2]
    except:
        await bot.send_message(message.chat.id, 'Пожалуйста введите ссылку на карту,кошелек и тд')
    else:
        if int(money) == 500 or int(money) > 500 and link != '' and int(balance) >= 500:
            add_money(int(select_balance(chat_id)) - int(money), chat_id)
            insert_get(message.chat.id, money, link)
        elif int(money) < 500 and link != '':
            await bot.send_message(message.chat.id, 'Сумма должна быть равна 500 или больше 500 руб')


@dp.message_handler(regexp='🏧 Баланс')
async def balance(message: Message):
    user_id = message.from_user.id
    balance = select_balance(user_id)
    await message.answer(f'''
    Ваш баланс: {balance}₽
    Делайте больше задание получить больше денег!
        ''')


@dp.message_handler(regexp='💸 Вывод')
async def get(message: Message):
    try:
        if select_banned_id(message.from_user.id):
            await message.answer('Вы забанены и не можете управлять ботом')
    except:

        await message.answer("""
        Мы выводим ваши рубли на эти банковские системы: 
        🥝QIWI , 💲Яндекс.Деньги, 🏧СберБанк и ⬛Tinkoff

        ☣ Если вы введете не правильный данный вашей системы то деньги будут переведены не на ваш счет!
        Администрация не введет отвественность за ваши ошибки!

        Ввыберите платежную систему:
            """, reply_markup=conclusion_start())


@dp.message_handler(regexp='☎ Поддержка')
async def help(message: Message):
    try:
        if select_banned_id(message.from_user.id):
            await message.answer('Вы забанены и не можете управлять ботом')
    except:

        await message.answer("""
    👨‍💻 Написать в поддержку - @buffalo_helpbot
    
    📂 Для того, что бы успешно вывести средства - надо соблюдать правила бота
    
    🪙 Ваш аккаунт должен быть правильно оформлен - должна стоять аватарка, нормальное имя и фамилия. Необязательно, что бы они были настоящими - главное, что бы выглядели нормально (например Иван Иванов). 
    
    🪙 После подписки на канал надо регулярно смотреть посты.
    
    🪙Когда вы получаете задания - вы видите правила его выполнения. Запрещено их нарушать.
    
    🪙 Не блокируйте бота до того момента, пока не выведете средства. 
    
    🪙 Если вам пишут с предложениями вывести заработанные деньги, предварительно заплатив - это мошенники. Будьте внимательны. Бот не взимает платы нигде, даже при выводе заработанных денег.
    
    🪙 Минимальный вывод ограничен 500₽. Суммы меньше мы пока не можем обрабатывать в связи с тем, что появится огромное количество заявок на вывод совсем маленьких сумм и огромных комиссиях на вывод.
    
    🪙 Вывод осуществляется на Qiwi, Яндекс.Деньги и Сбербанк.
    
    🪙 Если вы столкнетесь с проблемами при выводе - не переживайте. Мы сами попытаемся вывести средства несколько раз и если у нас не получится - мы свяжемся с вами.
    
    🪙 Если вы нарушили правила - вывод не пройдет. Мы не блокируем пользователей, которые нарушают правила, поэтому вы можете начать сначала.
    
    🪙 Если вы хотите купить добавление в задания, рассылку или такой же бот - пишите на рекламный контакт, он указан в описании бота.
    
    🪙 Пользователи, которые присоединяются в бот по вашей ссылке должны выполнить минимум одно задание, а лучше несколько. Если они этого не сделают - средства не будут выведены.
    """, reply_markup=helpp())


@dp.callback_query_handler(lambda call: 'qiwi' in call.data)
async def qiwia(call: CallbackQuery):
    if int(select_ref(call.message.chat.id)) == 5 or int(select_ref(call.message.from_user.id)) > 5:

        await bot.send_message(call.message.chat.id, '''Пожалуйста отправьте вашу ссылку на QIWI через /get количество денег ваша ссылка  для вывода
                                Вывод будет осуществлен в течении 24 часов 
                                Пример для вывода: /get 500 https://qiwi.com/n/REYNTT  '''
                               )
    else:
        await bot.send_message(call.message.chat.id,
                               'Вы должны иметь 5 приглошенных друзей иначе вывод не будет осуществлен!')


@dp.callback_query_handler(lambda call: 'yandex' in call.data)
async def yandexa(call: CallbackQuery):
    if int(select_ref(call.message.chat.id)) == 5 or int(select_ref(call.message.from_user.id)) > 5:
        await bot.send_message(call.message.chat.id,
                               '''Пожалуйста отправьте вашу ссылку на ЮМани через /get количество денег ваша ссылка  для вывода
                                                               Вывод будет осуществлен в течении 24 часов 
                                                               Пример для вывода: /get 500 https://qiwi.com/n/REYNTT  '''
                               )

    else:
        await bot.send_message(call.message.chat.id,
                               'Вы должны иметь 5 приглошенных друзей иначе вывод не будет осуществлен!')


@dp.callback_query_handler(lambda call: 'sberbank' in call.data)
async def sberbanka(call: CallbackQuery):
    if int(select_ref(call.message.chat.id)) == 5 or int(select_ref(call.message.from_user.id)) > 5:
        await bot.send_message(call.message.chat.id,
                               '''Пожалуйста отправьте вашу ссылку на SberBank через /get количество денег ваша ссылка  для вывода
                                                               Вывод будет осуществлен в течении 24 часов 
                                                               Пример для вывода: /get 500 https://qiwi.com/n/REYNTT  '''
                               )

    else:
        await bot.send_message(call.message.chat.id,
                               'Вы должны иметь 5 приглошенных друзей иначе вывод не будет осуществлен!')


@dp.callback_query_handler(lambda call: 'tinkoff' in call.data)
async def tinkoff(call: CallbackQuery):
    if int(select_ref(call.message.chat.id)) == 5 or int(select_ref(call.message.from_user.id)) > 5:
        await bot.send_message(call.message.chat.id,
                               '''Пожалуйста отправьте вашу ссылку на Тинькофф через /get количество денег ваша ссылка  для вывода
                                                               Вывод будет осуществлен в течении 24 часов 
                                                               Пример для вывода: /get 500 https://qiwi.com/n/REYNTT  '''
                               )

    else:
        await bot.send_message(call.message.chat.id,
                               'Вы должны иметь 5 приглошенных друзей иначе вывод не будет осуществлен!')


@dp.message_handler(regexp='👥 Рефералы')
async def referal(message: Message):
    if message.chat.type == 'private':
        try:
            if select_banned_id(message.from_user.id):
                await message.answer('Вы забанены и не можете управлять ботом')
        except:
            messag = message.from_user.id
            await message.answer(f'''
    Ваш ID: {message.from_user.id}\nhttps://t.me/{BOT_NAME}?start={message.from_user.id}\nКол-во Рефералов: {select_ref(messag)}
            ''')


@dp.message_handler(regexp='🧾 Выполнить задание')
async def get_task(message: Message):
    if message.chat.type == 'private':
        try:
            if select_banned_id(message.from_user.id)[0]:
                await message.answer('Вы забанены и не можете управлять ботом')
        except:
            for i, link in enumerate(CHANNEL_LINKS["channels"]):
                if not check_sub(await bot.get_chat_member(chat_id=link, user_id=message.from_user.id)):
                    await bot.send_message(message.chat.id, f"""
        Ваш приз: {select_money(link)}
        Подпишитесь на канал и получите деньги""", reply_markup=start_work(i))
                    break
            else:
                f = 2
                for i, link in enumerate(CHANNEL_LINKS["links"]):
                    await bot.send_message(message.chat.id, f"""
        Зарегистрируетесь на сайте
        Отправьте фото о профиле и получите {select_money_site(link)}
         """, reply_markup=start_work(i, link))
                    continue


@dp.callback_query_handler(lambda call: 'donejob' in call.data)
async def proverka(call: CallbackQuery):
    if call.message.chat.type == 'private':

        for i, link in enumerate(CHANNEL_LINKS['channels']):
            channel_id = call.data.split('_')[1]
            money = select_money(link)

            channel_link = select_link_channel(channel_id)

            chat_id = call.message.chat.id

        if not check_sub(await bot.get_chat_member(chat_id=channel_link, user_id=call.message.chat.id)):
            await bot.send_message(call.message.chat.id, 'Подпишитесь иначе вам не будет зачислены деньги!',
                                   reply_markup=start_work(int(channel_id) - 1))

        elif check_sub(await bot.get_chat_member(chat_id=channel_link, user_id=call.message.chat.id)):
            await bot.send_message(call.message.chat.id, f'Поздравляю вы получили: {select_money(channel_link)}₽')

            add_money(int(money) + select_balance(chat_id), chat_id)




@dp.callback_query_handler(lambda call: 'skip' in call.data)
async def check_user_send_photo(call: CallbackQuery):
    id_ = call.data.split('_')[1]
    print(id_)
    try:
        if select_banned_id(call.message.chat.id)[0]:
            await bot.send_message(call.message.chat.id,'Вы забанены и не можете управлять ботом')
    except:
        try:

            if not check_sub(await bot.get_chat_member(chat_id=select_link(int(id_)+2), user_id=call.message.chat.id)):
                await bot.send_message(call.message.chat.id, f"""
        Ваш приз: {select_money_id(int(id_)+2)}
        Подпишитесь на канал и получите деньги""", reply_markup=start_work(int(id_)+1))

        except:
            f = 2
            for i, link in enumerate(CHANNEL_LINKS["links"]):
                await bot.send_message(call.message.chat.id, f"""
    Зарегистрируетесь на сайте
    Отправьте фото о профиле и получите {select_money_site(link)}
     """, reply_markup=start_work(i, link))
                continue


@dp.callback_query_handler(lambda call: 'job' in call.data)
async def check_user_send_photo(call: CallbackQuery):
    link = call.data.split('_')[1]
    await bot.send_message(call.from_user.id,
                           f"Отправьте фото вашего профиля с ссылкой на сайт без каких либо букв иначе деньги не будут переведены вам! ссылка: {link}  ")


@dp.message_handler(content_types=['photo'])
async def send_photo_to_admin_group(message: Message):
    await bot.send_message(message.from_user.id, 'Было отправлено на проверку')
    await bot.send_photo("@hhfhhhfff", message.photo[0].file_id, f'{message.from_user.id}, {message.caption}',
                         reply_markup=check_photo())


@dp.callback_query_handler(lambda call: 'confirmed' in call.data)
async def confirm_photo_from_user_done(call: CallbackQuery):
    link = call.message.caption[11:]
    user_id = call.message.caption[0:9]
    try:
        if select__url(link):
            await bot.send_message(user_id, "Ваша заявка принята")
            add_link_(int(select_link_id(user_id)) + 1, user_id)
            add_money(int(select_money_site(link)) + select_balance(user_id), user_id)
    except:
        await bot.send_message(user_id, 'Неправильные адрес!')


@dp.callback_query_handler(lambda call: 'go' in call.data)
async def go_(call: CallbackQuery):
    try:
        if select_banned_id(call.message.from_user.id):
            await call.message.answer('Вы забанены и не можете управлять ботом')
    except:
        for i, link in enumerate(CHANNEL_LINKS["channels"]):
            if not check_sub(await bot.get_chat_member(chat_id=link, user_id=call.message.from_user.id)):
                await bot.send_message(call.message.chat.id, f"""
    Ваш приз: {select_money(link)}
    Подпишитесь на канал и получите деньги""", reply_markup=start_work(i))
                break
        else:
            for i, link in enumerate(CHANNEL_LINKS["links"]):
                await bot.send_message(call.message.chat.id, f"""
    Зарегистрируетесь на сайте
    Отправьте фото о профиле и получите {select_money_site(link)}
     """, reply_markup=start_work(i, link))
                continue


@dp.callback_query_handler(lambda call: 'rejected' in call.data)
async def confirm_photo_from_user_rejected(call: CallbackQuery):
    await bot.send_message(call.message.caption, "Ваша заявка отклонена, попробуйте снова")


@dp.message_handler(commands=['admin'], user_id=['631357872', '710258253', '527265470'])
async def admin(message: Message):
    await message.answer(f'''Здравствуйте {message.from_user.first_name} чем могу быть полезень
Список команд: /ban user_id 
Если user_id не тот то будет писать что нету такого пользователя если он есть то пользователь не сможет пользоваться функционалом
/add_money user_id сумма учтите что юзеру добавиться сумма
/stat - Количество пользователей 
/add_channel стоимость, link, время , ссылка
например /add_channel 99 @chdhhdf 1 https://t.me/chdhhdf

''',
                         reply_markup=adminn())


@dp.message_handler(commands=['ban'], user_id=['631357872', '710258253', '527265470'])
async def ban_user(message: Message):
    user_id = message.text[5:]
    if user_id == '':
        await message.answer('Напишите айди! /ban user_id ')
    else:
        if select_user_id(user_id):
            add_banned(user_id)
            await message.answer('Человек забанен')
        else:
            await message.answer('Такого пользователя не существует в боте')


@dp.message_handler(commands=['add_money'], user_id=['631357872', '710258253', '527265470'])
async def ban_user(message: Message):
    user_id = message.text.split(' ')[1]
    money = message.text.split(' ')[2]
    if select_user_id(user_id):
        add_money(int(select_balance(user_id)) + int(money), user_id)
        await message.answer('Успешно добавили деньги!')
    else:
        await message.answer('Такого пользователя не существует')


# @dp.callback_query_handler(lambda call: '')

@dp.callback_query_handler(lambda call: 'get' in call.data, user_id='631357872')
async def get(call: CallbackQuery):
    for user_id, price, link in select_all():

        try:
            await bot.send_message(call.message.chat.id, f'''
        Ид: {user_id}
        Вывод: {price}
        ''', reply_markup=get_money_admin(link, user_id))
            continue
        except:
            await bot.send_message(user_id, 'Вы ввели не правильный url')



@dp.callback_query_handler(lambda call: 'gone_pay' in call.data, user_id=['631357872', '527265470'])
async def get(call: CallbackQuery):
    user_id = call.data.split('_')[2]
    await bot.send_message(user_id, 'Оплата проведена успешно пожалуйста проверьте счет')


@dp.message_handler(commands=['stat'], user_id=['631357872', '710258253', '527265470'])
async def info_user(message: Message):
    for user_id, balance, name in select_info():
        await message.answer(f'''
Ид пользователя: {user_id}
Баланс: {balance}
Имя: {name}

''')


@dp.message_handler(commands=['add_promo'], user_id=['527265470', '631357872'])
async def add_promocod(message: Message):
    promocod = message.text.split(' ')[1]
    print(promocod)
    price = message.text.split(' ')[2]
    add_promo(promocod, price)
    await message.answer('Добавление было успешно')


@dp.message_handler(commands=['promo'])
async def promo(message: Message):
    promocod = message.text[7:]
    try:
        select_promo(promocod)
    except:
        await message.answer('Такого промокода не существует')
    else:
        try:
            select_history_promo(promocod) == promocod
        except:
            await message.answer('Вы уже использовали промокод')
        else:

            try:
                add_history_promo(message.chat.id, promocod)
            except:
                await message.answer('Вы уже использовали промокод')
            else:

                await message.answer(f'Поздравляю вы получили {select_price(promocod)}')
                add_money(int(select_balance(message.chat.id)) + int(select_price(promocod)), message.chat.id)


@dp.message_handler(commands=['add_channel'])
async def add_channel_in_base(message: Message):
    price = message.text.split(' ')[1]
    link = message.text.split(' ')[2]
    time = message.text.split(' ')[3]
    url = message.text.split(' ')[4]
    insert_channel(price, link, time, url)
    CHANNEL_LINKS['channels'].append(link)


@dp.message_handler(commands=['add_site'])
async def add_link_in_base(message: Message):
    price = message.text.split(' ')[1]
    link = message.text.split(' ')[2]
    time = message.text.split(' ')[3]
    insert_site(price, link, time)
    CHANNEL_LINKS['links'].append(link)


@dp.message_handler(commands=['delete_channel'])
async def delete_channel_in_base(message: Message):
    link = message.text.split(' ')[1]
    delete_channel(link)
    CHANNEL_LINKS['channels'].remove(link)


@dp.message_handler(commands=['delete_link'])
async def delete_link_in_base(message: Message):
    link = message.text.split(' ')[1]
    delete_site(link)
    CHANNEL_LINKS['links'].remove(link)

executor.start_polling(dp, skip_updates=True)
