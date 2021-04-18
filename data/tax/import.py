from dotenv import load_dotenv
import glob
import sqlite3
import csv
load_dotenv()

con = sqlite3.connect('../../data.sqlite')

files = glob.glob("*.csv")

cur = con.cursor()

for f in files:
    print('Processing: %s' % f)
    with open(f, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        cur.executemany("INSERT INTO tax VALUES (?,?,?,?,?,?,?,?,?)", csv_reader)
        con.commit()
con.close()