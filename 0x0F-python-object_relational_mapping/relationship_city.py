#!/usr/bin/python3
"""
Model city declaraive base

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
