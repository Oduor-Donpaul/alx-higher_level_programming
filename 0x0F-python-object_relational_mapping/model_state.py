#!/usr/bin/python3
""" Define the state model """

from sqlalchemy import Column, Integer, String
from sqlalcheny.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
  """ State class inheriting frong Base class

  Args:
      __tablename__(str): name of the table
      id(int)           : table's primary key
      name(str)         : state name
  """
  __tablename__ = "states"
  id = Column(Integer, Primary_key=True, nullable=False, autoincrement=True)
  name = Column(String,(128), nullable=False)
