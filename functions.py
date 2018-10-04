import sqlite3
import datetime

def register(bikeid, name, phonenumber, securitycode):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES (?, ?, ?, ?, 0, '00:00:00 01-01-1990')", (bikeid, name, phonenumber, securitycode,))
    conn.commit()
    conn.close()

def checkin(bikeid):
    conn = sqlite3.connect('database.db')
    curtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c = conn.cursor()
    c.execute("UPDATE data SET checkedin = 1, time = ? WHERE bikeid = ?", (curtime, bikeid,))
    conn.commit()
    conn.close()

def checkout(bikeid):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE data SET checkedin = 0 WHERE bikeid = ?", (bikeid,))
    conn.commit()
    conn.close()

def fetchpersonalinfo(bikeid):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * from data where bikeid = ?", (bikeid,))
    conn.commit()
    result = c.fetchone()
    if result:
        return result
    else:
        return False
    conn.close()

def securitycode(bikeid, securitycode):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT bikeid,securitycode from data where bikeid = ? AND securitycode = ?", (bikeid, securitycode))
    conn.commit()
    result = c.fetchone()
    if result:
        return True
    else:
        return False
    conn.close()

# Berry https://pypi.org/project/captcha/0.2.4/
#def captcha():

# Berry https://github.com/pyotp/pyotp
#def twofactorauthentication:

# Berry https://pythonhosted.org/python-pushover/
#def pushovernotification():