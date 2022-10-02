from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from work import *


def main():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='🧾 Выполнить задание')],
        [KeyboardButton(text='🏧 Баланс'), KeyboardButton(text='💸 Вывод')],
        [KeyboardButton(text='👥 Рефералы'), KeyboardButton(text='☎ Поддержка'),KeyboardButton(text='🎞 Промокоды')]
    ], resize_keyboard=True)


def start_work(channel_id='', url=''):
    markup = InlineKeyboardMarkup()
    tipe = 'channel'

    if not url:
        job = select_url(tipe)[channel_id]
        buttons = [
            InlineKeyboardButton(text='🚀 Канал', callback_data=f"channel_{job[1]}", url=f'''{job[0]}'''),
            InlineKeyboardButton(text='✅ Выполнено', callback_data=f"donejob_{job[1]}"),
            InlineKeyboardButton(text='Пропустить',callback_data=f'skip_{channel_id}')
        ]

    else:
        buttons = [
            InlineKeyboardButton(text='🚀 Сайт', callback_data=f"channel_{channel_id}", url=f'''{url}'''),
            InlineKeyboardButton(text='✅ Выполнено', callback_data=f"job_{url}")
        ]

    markup.add(*buttons)
    return markup
def back(link):
    markup = ReplyKeyboardMarkup()
    markup.add(
        KeyboardButton(text='Назад', callback_data=f"back_{link}")
    )
    return markup
def continue_get(link):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Продолжить', callback_data=f"continue_{link}")
    )
    return markup

def conclusion_start():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='🥝QIWI ', callback_data="qiwi"),
        InlineKeyboardButton(text='💲Яндекс.Деньги', callback_data="yandex"),
        InlineKeyboardButton(text='🏧СберБанк', callback_data='sberbank'),
        InlineKeyboardButton(text='⬛Tinkoff', callback_data='tinkoff')
    )
    return markup


def go(channel_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Продолжить', callback_data=f'go_{channel_id}'),
        InlineKeyboardButton(text='Назад', callback_data=f'back_{channel_id}'),

    )
    return markup


def helpp():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Тех.Поддержка', callback_data='helper', url='https://t.me/buffalo_helpbot')
    )
    return markup
def get_money_admin(link, id_):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Оплата', callback_data='give_money', url=f'{link}'),
        InlineKeyboardButton(text='Отказ', callback_data=f'no_money_{id_}'),
        InlineKeyboardButton(text='Готово',callback_data=f'gone_pay_{id_}')
    )
    return markup


def adminn():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Заявки для вывода', callback_data='get')
    )
    return markup


def check_photo():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text='Подтвердить', callback_data=f"confirmed"),
        InlineKeyboardButton(text='Отказать', callback_data=f"rejected")
    )
    return markup
