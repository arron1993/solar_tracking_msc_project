import argparse
import sqlite3
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", help="File Name")
args = parser.parse_args()
conn = sqlite3.connect(args.file_name+".db")
c = conn.cursor()



f = open('DAT_CH0.csv', 'w')

for row in c.execute("SELECT * FROM readings WHERE channel = 0"):
    time = datetime.datetime.fromtimestamp(int(row[0])).strftime('%H:%M:%S')
    voltage = row[5]
    to_write = "{},{}\n".format(time,voltage)
    f.write(to_write)

f.close()


f = open('Fixed_CH1.csv', 'w')
for row in c.execute("SELECT * FROM readings WHERE channel = 1"):
	time = datetime.datetime.fromtimestamp(int(row[0])).strftime('%H:%M:%S')
	voltage = row[5]
	to_write = "{},{}\n".format(time,voltage)
	f.write(to_write)
f.close()

f = open('SAT_CH2.csv', 'w')
for row in c.execute("SELECT * FROM readings WHERE channel = 2"):
	time = datetime.datetime.fromtimestamp(int(row[0])).strftime('%H:%M:%S')
	voltage = row[5]
	to_write = "{},{}\n".format(time,voltage)
	f.write(to_write)

f.close()
c.close()
