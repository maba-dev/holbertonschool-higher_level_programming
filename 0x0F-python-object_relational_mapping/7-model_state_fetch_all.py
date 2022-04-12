#!/usr/bin/python3
"""use the module SQLAlchemy """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import Session
from model_state import State
Base = declarative_base()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
