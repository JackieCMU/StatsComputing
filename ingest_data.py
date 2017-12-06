import csv
import sys
import psycopg2
from datetime import date
from helperFunction import *

def ingest():
    time = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day)
    conn = psycopg2.connect(host = 'sculptor.stat.cmu.edu', database = 'jiaqih1', user = 'jiaqih1', password = 'eu2Uenais')
    cur = conn.cursor()
    reader = csv.reader(sys.stdin, delimiter=',')
    corrected = 0
    for row in reader:
        valueDict, script = match(row)
        cur.execute(script)
        catchneighbor = [neighbor[0] for neighbor in cur.fetchall()]
        if len(catchneighbor) == 0:
            with open(time + '_ingest_error.txt', 'a') as txtfile:
                writer2 = csv.writer(txtfile)
                writer2.writerow(row)
        else:
            if valueDict['neighborhood'] != catchneighbor[0]:
                valueDict['neighborhood'] = catchneighbor[0]
                corrected += 1
            try:
                cur.execute("INSERT INTO blotter (" + ", ".join(valueDict.keys()) + ")"
                "VALUES (" + ",".join(["%(" + value + ")s" for value in valueDict]) + ");",
                valueDict)
                conn.commit()
            except psycopg2.DatabaseError as error:
                with open(time + '_ingest_error.txt', 'a') as txtfile:
                    writer2 = csv.writer(txtfile)
                    writer2.writerow(row)
                conn.rollback()
    conn.close()
    print(corrected)

ingest()
