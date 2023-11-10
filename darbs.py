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
                    epasts TEXT NOT NULL
                )
                ''')

# izveido otru tabulu ar relaciju

cursor.execute('''
                CREATE TABLE IF NOT EXISTS pasutijumi(
                    id INTEGER PRIMARY KEY,
                    lietotaja_id INTEGER,
                    produkta_nosaukums TEXT NOT NULL,
                    daudzums INTEGER NOT NULL,
                    FOREIGN KEY (lietotaja_id) REFERENCES lietotaji(id)
                )   
                ''')

# ievieto datus lietotaju tabula
cursor.execute("INSERT INTO lietotajs (vards, uzvards, epasts) VALUES (?,?,?)", ('Juris', 'Berzns', 'janis.berzins@p.lv'))
cursor.execute("INSERT INTO lietotajs (vards, uzvards, epasts) VALUES (?,?,?)", ('janis', 'Berzns', 'janis2.berzins@p.lv'))

# ievieto datus pasutitaju tabula
cursor.execute("INSERT INTO pasutijumi (lietotaja_id, produkta_nosaukums, daudzums) VALUE (?,?,?)", (1, 'dators', 2))
cursor.execute("INSERT INTO pasutijumi (lietotaja_id, produkta_nosaukums, daudzums) VALUE (?,?,?)", (2, 'televizors', 1))








conn.commit()
conn.close()
