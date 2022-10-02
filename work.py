import sqlite3


def select_info():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''SELECT user_id, balance, name FROM users''').fetchall()
    database.close()
    return result


def user_exists(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute("SELECT * FROM 'referal' WHERE 'user_id' = ?", (user_id,)).fetchall()

    return bool(len(result))


def select_user_id(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
SELECT user_id FROM users WHERE user_id = ?
    ''', (user_id,))
    return result


def insert_get(user_id, price, link):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
INSERT INTO get_money(user_id, price, link) VALUES(?,?,?)
    ''', (user_id, price, link))
    database.commit()
    return result


def add_banned(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
INSERT INTO banned_users(user_id) VALUES(?)''', (user_id,))
    database.commit()
    return result


def add_user(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('INSERT INTO referal("user_id") VALUES (?) ', (user_id,))
    database.commit()
    return result


def add_user_ref(user_id, referrer_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()

    result = cursor.execute('INSERT INTO referal(user_id,referrer_id) VALUES(?,?)', (user_id, referrer_id,))
    database.commit()
    return result


def select_ref(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute("SELECT COUNT(id) as count FROM referal WHERE referrer_id = ?", (user_id,)).fetchone()[0]

    return result


def add_users(user_id, name):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    INSERT INTO 'users'('user_id', 'name') VALUES(?,?)
    ''', (user_id, name))
    database.commit()
    return result


def select_balance(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT balance FROM users WHERE user_id = ?
    ''', (user_id,)).fetchone()[0]
    return result


def add_money(sum_, user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE users SET balance = ? WHERE user_id = ?
    ''', (sum_, user_id))
    database.commit()
    database.close()


def add_link_(sum_, user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE users SET link_id = ? WHERE user_id = ?
    ''', (sum_, user_id))
    database.commit()
    database.close()


def select_url(tipe):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT url, channel_id  FROM job WHERE tipe = ? ''', (tipe,)).fetchall()
    return result


def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


def select_all():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT user_id,price,link FROM get_money 
    ''').fetchall()
    return result

def select_link(channel_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT link FROM job WHERE channel_id = ?
    ''', (channel_id,)).fetchone()[0]
    return result


def select_money(channel_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
   SELECT price FROM job WHERE link = ?
   ''', (channel_id,)).fetchone()[0]
    # print(result)
    return result
def select_money_id(id_):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
   SELECT price FROM job WHERE channel_id = ?
   ''', (id_,)).fetchone()[0]
    # print(result)
    return result


def select_link_channel(channel_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT link FROM job WHERE channel_id  = ?
    ''', (channel_id,)).fetchone()[0]
    # print(result)
    return result


def select_money_site(channel_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
   SELECT price FROM site WHERE link = ?
   ''', (channel_id,)).fetchone()[0]
    # print(result)
    return result


def select_link_id(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
SELECT link_id FROM users WHERE user_id = ?
    ''', (user_id,)).fetchone()[0]
    return result


def select_id_():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT channel_id FROM job
    ''').fetchone()
    result = result[-1]
    return result


def select_tipe(link):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT tipe FROM job WHERE link = ?
    ''', (link,)).fetchone()[0]
    return result


def select_banned_id(id_):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT user_id FROM banned_users WHERE user_id = ?
    ''', (id_,)).fetchone()
    return result


def select__url(url):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT link FROM site WHERE link = ?
    ''', (url,)).fetchone()[0]
    return result


def select_linkk(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute("SELECT COUNT(channel_id) as count FROM job WHERE 'tipe' = 'site' ", (user_id,))
    return result


def add_history_promo(user_id, promo):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
        INSERT INTO history_promo(user_id,promocod) VALUES(?,?)
        ''', (user_id, promo))
    database.commit()


def select_history_promo(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
            SELECT promocod FROM history_promo WHERE promocod = ?
            ''', (user_id,)).fetchone()
    return result

def select_historypromo(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    try:
        result = cursor.execute('''
            SELECT user_id FROM history_promo WHERE promocod = ?
            ''', (user_id,)).fetchone()[0]
    except:
        return False
    else:
        return result


def add_promo(name_promo, price):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()

    cursor.execute('''
    INSERT INTO promo(promo, price) VALUES(?,?) 
    ''', (name_promo, price,))
    database.commit()


def select_promo(promo):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT promo FROM promo WHERE promo = ?
    ''', (promo,)).fetchone()[0]
    return result


def select_price(promo):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT price FROM promo WHERE promo = ?
    ''', (promo,)).fetchone()[0]
    return result
#
# def link_(link,user_id):
#     if link == select_link_rejected(link, user_id):
#         link[+1]
#     else:


def select_link_rejected(link,user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute('''
    SELECT link FROM rejected WHERE link = ? and user_id = ?
    ''', (link,user_id)).fetchone()
    return result
def insert_channel(price, link, time, url):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    channel = 'channel'
    cursor.execute('''
    INSERT INTO job(price,link,time,url,tipe) VALUES(?,?,?,?,?)
    ''', (price, link, time, url, channel))
    database.commit()
def insert_rejected(user_id, link):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO rejected(user_id,link) VALUES(?,?)
    ''', (user_id, link))
    database.commit()


def insert_site(price, link, time):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO site(price,link,time) VALUES(?,?,?)
    ''', (price, link, time))
    database.commit()


def delete_channel(link):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
   DELETE FROM job
    WHERE link = ?
    ''', (link))
    database.commit()


def delete_site(link):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
   DELETE FROM site
    WHERE link = ?
    ''', (link))
    database.commit()
#
#
# def insert_cancel_user_id(user_id):
#     database = sqlite3.connect('database_buffalo.db')
#     cursor = database.cursor()
#     cursor.execute('''
#     INSERT INTO cancel_(user_id) VALUES(?)
#     ''', (user_id))
#     database.commit()
#     database.close()
#
#
# def insert_cancel_link(link, status, user_id):
#     database = sqlite3.connect('database_buffalo.db')
#     cursor = database.cursor()
#     cursor.execute('''
#     UPDATE cancel_ SET link = ? and status=? WHERE user_id = ?
#     ''', (link, status, user_id))
#     database.commit()
#     database.close()
