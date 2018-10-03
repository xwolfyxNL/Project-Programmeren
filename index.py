import csv
import os.path

if os.path.exists('database.csv') == False:
    with open('database.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['bikeID', 'Name', 'Phonenumber', 'Securitycode', 'Registered', 'Time'])
        # test data
        filewriter.writerow(['14378427', 'Henk van de Piet', '12345678', 'koe', '', ''])
        filewriter.writerow(['93247234', 'Jan van de Brug', '87654321', 'bruggetje', '', ''])
        filewriter.writerow(['23022372', 'Janieta van de Dood', '82748234', 'makeup', '', ''])
        print('Database has been created')
else:
    print('Database already exists')