#!/usr/bin/python3
"""use the module SQLAlchemy """
from unicodedata import name
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State
Base = declarative_base()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for (city, state) in session.query(City, State).where(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
