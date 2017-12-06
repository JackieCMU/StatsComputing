import psycopg2
import csv
import sys
from datetime import date
from helperFunction import *

def patch():
    time = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day)
    conn = psycopg2.connect(host = 'sculptor.stat.cmu.edu', database = 'jiaqih1', user = 'jiaqih1', password = 'eu2Uenais')
    cur = conn.cursor()
    cur.execute("SELECT id FROM blotter;")
    reader = csv.reader(sys.stdin, delimiter=',')
    idList = [id[0] for id in cur.fetchall()]
    corrected, p = 0, 0
    for row in reader:
        valueDict, script = match(row)
        cur.execute(script)
        catchneighbor = [neighbor[0] for neighbor in cur.fetchall()]
        if len(catchneighbor) == 0:
            with open(time + '_patch_error.txt', 'a') as csvfile:
                writer3 = csv.writer(csvfile)
                writer3.writerow(row)
        else:
            if valueDict['neighborhood'] != catchneighbor[0]:
                valueDict['neighborhood'] = catchneighbor[0]
                row[6] = catchneighbor[0]
                corrected += 1
            if valueDict['id'] not in idList:
                cur.execute("INSERT INTO blotter (" + ", ".join(valueDict.keys()) + ")"
                "VALUES (" + ",".join(["%(" + value + ")s" for value in valueDict]) + ");",
                valueDict)
            else:
                p += 1
                cur.execute("""UPDATE blotter
                SET report_name = %s,
                section = %s,
                description = %s,
                arrest_time = %s,
                address = %s,
                neighborhood = %s,
                zone = %s WHERE id = %s;""",
                row[1:]+[row[0]])
        conn.commit()
    conn.close()
    print(corrected)
    print(p)

valid_sections = ['3304','2709','3502','13(a)(16)','13(a)(30)','3701','3921',
            '3921(a)','3934','3929','2701','2702','2501']

patch()
