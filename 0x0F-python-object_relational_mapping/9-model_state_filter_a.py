#!/usr/bin/python3
'''Session query'''

import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dtbs = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, dtbs))
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(State).filter(State.name.like(
                                        '%a%')).order_by(State.id)
    for instance in Query:
        print("{0}: {1}".format(instance.id, instance.name))
