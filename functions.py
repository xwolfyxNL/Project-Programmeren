import sqlite3

def register():


def checkin(bikeID, name, phonenumber, Securitycode):
        with open('database.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for line in csvreader:



def checkout():

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

def securitycode(bikeID, securitycode):
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
def captcha():

# Berry https://github.com/pyotp/pyotp
def twofactorauthentication:

# Berry https://pythonhosted.org/python-pushover/
def pushovernotification():