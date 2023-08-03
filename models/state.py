#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # class attribute for DBStorage
    cities = relationship("City", back_populates="State")

    @property
    def cities(self):
        """Getter for FileStorage
        Returns a list of City instances with state_id = current State.id
        """
        from models.city import City    # import here to avoid circular import
        from models import storage
        cities_list = []
        for city in City.instances.values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
