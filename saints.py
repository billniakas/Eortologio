import sqlite3
sqlite_file = 'saints.db'
conn = sqlite3.connect(sqlite_file)

day=input("Δώσε μέρα : ")
month=input("Δώσε μήνα : ")


c = conn.cursor()

c.execute('SELECT * FROM Saints where day={} and month={} AND source like "saint.gr"'.format(day,month))
all_rows = c.fetchall()
for row in all_rows[0][0:-3]:
    print(row.replace("<b>"," ").replace("</b>"," "))

conn.close()
