#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.city import City
from models.user import User


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # class attribute for DBStorage
    cities = relationship("City", back_populates="State")

    @property
    def cities(self):
        """Getter for FileStorage"""
        pass
