import csv
import os.path

if os.path.exists('database.csv') == False:
    with open('database.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['bikeID', 'Name', 'Phonenumber', 'Securitycode', 'Registered', 'Time'])
else:
    print('okay')