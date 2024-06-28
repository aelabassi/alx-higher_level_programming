#!/usr/bin/python3
"""
    State table using sqlalchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
        State class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
