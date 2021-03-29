#!/usr/bin/python3
""" comment """

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]), pool_pre_ping="True")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = State(name="California")
    session.add(row)
    session.commit()
    new_city = City(name="San Francisco")
    row.cities.append(new_city)
    session.close()
