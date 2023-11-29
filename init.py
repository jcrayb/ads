import sqlite3 as sq3

con = sq3.connect('./db/ad.db', check_same_thread=False)
cur = con.cursor()

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