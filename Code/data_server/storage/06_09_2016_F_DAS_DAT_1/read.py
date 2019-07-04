import argparse
import sqlite3
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", help="File Name")
args = parser.parse_args()
conn = sqlite3.connect("692016.db")
c = conn.cursor()



f = open('02092016_DAS.csv', 'w')

for row in c.execute("SELECT * FROM readings WHERE channel = 0"):
    time = datetime.datetime.fromtimestamp(int(row[0])).strftime('%H:%M:%S')
    voltage = row[5]
    to_write = "{},{}\n".format(time,voltage)
    f.write(to_write)

f.close()


f = open('02092016_F.csv', 'w')
for row in c.execute("SELECT * FROM readings WHERE channel = 1"):
	time = datetime.datetime.fromtimestamp(int(row[0])).strftime('%H:%M:%S')
	voltage = row[5]
	to_write = "{},{}\n".format(time,voltage)
	f.write(to_write)
f.close()

f = open('02092016_SAS.csv', 'w')
for row in c.execute("SELECT * FROM readings WHERE channel = 2"):
	time = datetime.datetime.fromtimestamp(int(row[0])).strftime('%H:%M:%S')
	voltage = row[5]
	to_write = "{},{}\n".format(time,voltage)
	f.write(to_write)

f.close()
c.close()
