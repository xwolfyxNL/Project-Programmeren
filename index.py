import sqlite3
import os.path
from tkinter import *



if os.path.exists('database.db') == False:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE data
                 (bikeid INTEGER PRIMARY KEY ,name text, phonenumber text, securitycode text, checkedin INTEGER, time TEXT)''')
    c.execute("INSERT INTO data VALUES (83242, 'Henk Piet', '12345678', 'koe', 0, '00:00:00 01-01-1990')")
    c.execute("INSERT INTO data VALUES (43536, 'Rita Henksla', '87654321', 'eok', 0, '00:00:00 01-01-1990')")
    conn.commit()
    conn.close()
else:
    print('Database exists')

root = Tk()
root.geometry("250x400")


registerbut = Button(master=root, text='Registreren')
checkinbut = Button(master=root, text='Inchecken')
checkoutbut = Button(master=root, text='Uitchecken')
registerbut.pack(pady=10)
checkinbut.pack(pady=50)
checkoutbut.pack(pady = 30)



root.mainloop()
