import sqlite3 as sq3

con = sq3.connect('./db/ad.db', check_same_thread=False)
cur = con.cursor()


def initalize():
    try:
        cur.execute('''CREATE TABLE visits(
                id VARCHAR,
                date VARCHAR,
                origin VARCHAR
            )''')
    except:
        pass

    try:
        cur.execute('''CREATE TABLE ads(
                id VARCHAR,
                url VARCHAR
            )''')
    except:
        pass

    if not cur.execute('SELECT * FROM ads WHERE id="1"').fetchone():
        cur.execute('INSERT INTO ads VALUES ("1", "https://jcrayb.com")')
        print("1")

    if not cur.execute('SELECT * FROM ads WHERE id="6d2818f3"').fetchone():
        cur.execute('INSERT INTO ads VALUES ("6d2818f3", "https://jcrayb.com")')
        print("6d2818f3")
    
    con.commit()
    return