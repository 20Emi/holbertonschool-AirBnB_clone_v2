#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.environ.get('HBNB_TYPE_STORAGE'):
        name = Column(String(128), nullable=False)
        # class attribute for DBStorage
        cities = relationship("City", cascade="all, delete", backref="State")
    else:
        name = ''

    @property
    def cities(self):
        """Getter for FileStorage
        Returns a list of City instances with state_id = current State.id
        """
        from models.city import City    # import here to avoid circular import
        from models import storage
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
