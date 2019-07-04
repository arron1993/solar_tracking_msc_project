import argparse
import sqlite3
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", help="File Name")
args = parser.parse_args()
conn = sqlite3.connect(args.file_name+".db")
c = conn.cursor()



for row in c.execute("SELECT * FROM readings where angle_mode = 'DA-S'"):
        print(row)

c.close()
