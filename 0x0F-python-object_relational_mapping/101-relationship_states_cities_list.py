#!/usr/bin/python3
""" comment """

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy


if __name__ == "__main__":
    MY_DB = argv[3]
    MY_USER = argv[1]
    MY_PSW = argv[2]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PSW, MY_DB),
                           pool_pre_ping="True")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
