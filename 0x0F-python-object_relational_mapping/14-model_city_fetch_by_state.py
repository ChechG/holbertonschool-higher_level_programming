#!/usr/bin/python3
""" comment """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    c = City.state_id
    s = State.id
    r = session.query(City, State).filter(s == c).order_by(City.id)
    for city, state in r:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
