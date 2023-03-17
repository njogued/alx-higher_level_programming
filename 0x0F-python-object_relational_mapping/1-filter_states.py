#!/usr/bin/python3

import MySQLdb
import sys

try:
    usr = sys.argv[1]
    passwrd = sys.argv[2]
    dtbs = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passwrd, db=dtbs)
    cur = db.cursor
    cur.execute("SELECT * FROM states WHERE name = 'Arizona'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db,close()
except Exception as e:
    print(e)
