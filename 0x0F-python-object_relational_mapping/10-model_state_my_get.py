#!/usr/bin/python3
'''State object with the name'''
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv as av

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            av[1], av[2], av[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    search = av[4]
    instance = session.query(State).filter(State.name.like(search)).first()
    '''
    instance = session.query(State).filter(State.name == 'Texas').first
    instance = session.query(State).from_statement(text(
    "SELECT states.id FROM states WHERE name=:name")).params(
    name='Texas').all()
    '''
    if instance:
        print(f"{instance.id}")
    else:
        print("Not found")
