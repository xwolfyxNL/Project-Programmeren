import csv


def register():


def checkin(bikeID, name, phonenumber, Securitycode):
        with open('database.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for line in csvreader:



def checkout():

def fetchpersonalinfo():

def securitycode():

# Berry https://pypi.org/project/captcha/0.2.4/
def captcha():

# Berry https://github.com/pyotp/pyotp
def twofactorauthentication:

# Berry https://pythonhosted.org/python-pushover/
def pushovernotification():