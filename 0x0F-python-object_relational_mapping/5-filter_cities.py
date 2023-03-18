#!/usr/bin/python3
'''JOIN STATES ON STATES'''
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        dtbs = sys.argv[3]
        state = sys.argv[4]
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=dtbs
            )
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities JOIN states ON \
        states.id=cities.state_id WHERE states.name = '{}'".format(state))
        rows = cur.fetchall()
        print(', '.join(i[0] for i in rows))
        cur.close()
        db.close()
    except Exception as e:
        print(e)
