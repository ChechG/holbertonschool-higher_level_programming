#!/usr/bin/python3
""" comentario """
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy


class City(Base):
    """ comentario """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
