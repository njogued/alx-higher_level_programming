#!/usr/bin/python3
'''
Using MySQLdb
'''

import MySQLdb
import sys

try:
    usr = sys.argv[1]
    passwrd = sys.argv[2]
    dtbs = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=usr, passwd=passwrd, db=dtbs)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
except Exception as e:
    print(e)
