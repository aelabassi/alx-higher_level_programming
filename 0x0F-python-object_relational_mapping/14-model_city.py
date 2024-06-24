#!/usr/bin/python3
"""
setup model city engine
"""
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)

    if len(sys.argv) == 4:
        db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
        Base.metadata.create_all(db)
        session = sessionmaker(bind=db)
        session = session()
        for city, state in session.query(City.id, State.name, City.name)\
                .filter(
                City.state_id == State.id).all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))
