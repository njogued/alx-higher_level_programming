#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        dtbs = sys.argv[3]
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dtbs)
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print(e)
