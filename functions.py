import csv


def register():


def checkin(bikeID, name, phonenumber, Securitycode):
        with open('database.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for line in csvreader:



def checkout():

def fetchpersonalinfo():

def captcha():

def notification():

def securitycode():