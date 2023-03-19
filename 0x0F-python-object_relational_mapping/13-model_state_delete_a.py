#!/usr/bin/python3
'''
Delete a State object
'''
from model_state import Base, State
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker as sm
from sys import argv as v

if __name__ == "__main__":
    engine = ce(f"mysql+mysqldb://{v[1]}:{v[2]}@localhost:3306/{v[3]}")
    Session = sm(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(instance)
    session.commit()
