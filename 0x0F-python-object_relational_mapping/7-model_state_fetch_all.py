#!/usr/bin/python3
""" List all objects from database """

from modal_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
  engine = create_engine("mysql+mysqldb://{}:{}@localhost:3366/{}"
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]))
  Session = sessionmaker(bind=engine)
  session = Session()

  states_list = session.query(state).order_by(State.id).all()
  [print("{}: {}".format(state.id, state.name)) for state in state_list]
  session.close()
