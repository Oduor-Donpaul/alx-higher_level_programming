#!/usr/bin/python3
""" List all State objects from the database hbtn_0e_6_usa """

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id == "2").first()
    update.name = "New Mexico"
    session.add(update)
    session.commit()
    session.close()

