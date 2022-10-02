import sqlite3


def create_referral():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''                                                                                                                                   
    CREATE TABLE referal (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL
                        UNIQUE,
    referrer_id INTEGER
);

    ''')


def create_job():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE job (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        price INTEGER NOT NULL,
        link  TEXT,
        time  INTEGER,
        tipe       TEXT
    );

    ''')

def create_rejected():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE rejected (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    link    TEXT
);

    ''')


def create_site():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE site (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            price INTEGER NOT NULL,
            link  TEXT,
            time  INTEGER
        );

        ''')


def create_banned_users():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE banned_users (
        id_autoincrement INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id          INTEGER
    );

    ''')


def user_exists(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    result = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    return result

def create_get_money():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
        
CREATE TABLE get_money (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    price   INTEGER,
    link    TEXT,
    tipe    TEXT
);''')
    database.commit()
    database.close()

def add_user(user_id):
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()

    return cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))


def get_users():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    return cursor.execute("SELECT user_id FROM users").fetchall()



def create_promo():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
     CREATE TABLE promo(
        id_prime INTEGER PRIMARY KEY AUTOINCREMENT,
        promo TEXT,
        price INTEGER
    );
'''   )
    database.commit()

def create_history():
    database = sqlite3.connect('database_buffalo.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE history_promo(id_prime INTEGER,promocod TEXT, user_id INTEGER
    );
    ''')
    database.commit()

# create_history()
# create_promo()
