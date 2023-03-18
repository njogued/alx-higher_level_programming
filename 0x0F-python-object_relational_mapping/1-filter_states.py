#!/usr/bin/python3
'''
Using MySQLdb
'''

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        u = sys.argv[1]
        p = sys.argv[2]
        d = sys.argv[3]
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=u,
                passwd=p,
                db=d
                )
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE states.name \
LIKE BINARY 'N%' ORDER BY states.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print(e)
