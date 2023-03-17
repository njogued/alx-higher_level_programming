#!/usr/bin/python3

from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_0_usa')
states = engine.execute('SELECT * FROM states ORDER BY id')

for state in states:
    print(state)
