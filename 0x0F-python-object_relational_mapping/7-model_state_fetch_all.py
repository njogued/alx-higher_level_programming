#!/usr/bin/python3

import sys
import sqlalchemy
from model_state import State, Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dtbs = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}')

