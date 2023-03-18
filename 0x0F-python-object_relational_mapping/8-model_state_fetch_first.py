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
    instance = session.query(State).order_by(State.id).first()
    if instance:
        print("{0}: {1}".format(instance.id, instance.name))
    else:
        print("Nothing")
