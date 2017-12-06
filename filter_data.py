import csv
import sys
from datetime import date

def filter(filename, report_name, valid_sections):
    '''
    filename: csv file
    report_name: string, the report name
    '''
    # count = 0 # uncomment when testing
    time = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day)
    writer = csv.writer(sys.stdout, delimiter = ',')
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            reportName, section = row[1], row[2]
            if len(row) != 8 or reportName != "OFFENSE 2.0" or section not in valid_sections or any(row[i] == '' for i in range(8)):
                with open(time + '_filter_invalid_error.txt', 'a') as csvfile:
                    writer1 = csv.writer(csvfile)
                    writer1.writerow(row)
                continue
            writer.writerow(row)
            # count += 1 # uncomment when testing
    # return count # uncomment when testing

# Now run the main program
valid_sections = ['3304','2709','3502','13(a)(16)','13(a)(30)','3701','3921',
            '3921(a)','3934','3929','2701','2702','2501']
report_name = "OFFENSE 2.0"

filename = sys.argv[1] # comment when testing
filter(filename, report_name, valid_sections) # comment when testing
