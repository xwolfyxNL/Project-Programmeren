import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE data
             (bikeid INTEGER PRIMARY KEY ,name text, phonenumber text, securitycode text, checkedin INTEGER, time TEXT)''')
c.execute("INSERT INTO data VALUES (83242, 'Henk Piet', '12345678', 'koe', 0, '00:00:00 01-01-1990')")
c.execute("INSERT INTO data VALUES (43536, 'Rita Henksla', '87654321', 'eok', 0, '00:00:00 01-01-1990')")
conn.commit()
conn.close()