import sqlite3

# datu baze un japiesledzas tai
conn = sqlite3.connect('piemers.db')
cursor=conn.cursor()

# izveidot tabulu
cursor.execute('''
                CREATE TABLE IF NOT EXISTS lietotajs(
                    id INTEGER PRIMARY KEY,
                    vards TEXT NOT NULL,
                    uzvards TEXT NOT NULL,
                    epasts TEXT NOT NULL UNIQUE
                )
                ''')













conn.commit()
conn.close()
