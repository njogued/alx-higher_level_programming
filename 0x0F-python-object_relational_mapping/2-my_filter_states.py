#!/usr/bin/python3
'''Search and Order'''

import sys
import MySQLdb

if __name__ == "__main__":
    try:
        usr = sys.argv[1]
        passwrd = sys.argv[2]
        db_name = sys.argv[3]
        search = sys.argv[4]
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=usr,
            passwd=passwrd,
            db=db_name
            )
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
        ORDER BY states.id".format(search))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print(e)
