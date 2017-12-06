import psycopg2
import csv

conn = psycopg2.connect(host='sculptor.stat.cmu.edu', database='jiaqih1', user='jiaqih1', password='eu2Uenais')
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS neighborhoods CASCADE;
CREATE TABLE neighborhoods (
id INTEGER,
neighbor text PRIMARY KEY UNIQUE
);""")

cur.execute("""DROP TABLE IF EXISTS blotter CASCADE;
CREATE TABLE blotter (
id INTEGER PRIMARY KEY UNIQUE,
report_name TEXT DEFAULT 'OFFENSE 2.0',
section TEXT,
description TEXT,
arrest_time TIMESTAMP,
address TEXT,
neighborhood TEXT REFERENCES neighborhoods(neighbor),
zone INTEGER CHECK (zone > 0)
);""")

with open('data/police-neighborhoods.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        id_ = int(row[3])
        neighbor = row[2]
        location = [float(row[0]),float(row[1])]
        cur.execute("INSERT INTO neighborhoods (id, neighbor)"
                   "VALUES (%(id)s, %(neighbor)s)",
                   {'id': id_, 'neighbor': neighbor})

conn.commit()
conn.close()
