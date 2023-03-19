#!/usr/bin/python3

'''Update a state Object'''

from model_state import Base, State
from sqlalchemy.orm import sessionmaker as sm
from sqlalchemy import create_engine as ce
from sys import argv as v

if __name__ == "__main__":
    engine = ce(f"mysql+mysqldb://{v[1]}:{v[2]}@localhost:3306/{v[3]}")
    Session = sm(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.id == 2).first()
    instance.name = "New Mexico"
    session.commit()
