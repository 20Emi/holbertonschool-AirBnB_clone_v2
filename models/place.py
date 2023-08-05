#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # for DBStorage
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    # for FileStorage

    @property
    def reviews(self):
        """Getter for FileStorage
        """
        # imports here to avoid circular import
        from models.place import Place
        from models import storage
        reviews_list = []
        for review in storage.all(Place).values():
            if Place.state_id == self.id:
                reviews_list.append(Place)
        return reviews_list

    # for DBStorage task 10
    amenities = relationship(
        'Amenity', secondary='place_amenity', viewonly=False)

    # Getter task 10
    @property
    def amenities(self):
        """Getter for FileStorage
        """
        # import here to avoid circular import
        from models.amenity import Amenity
        from models import storage
        amenities_list = []
        for amenities in storage.all(Amenity).values():
            if amenities.id == self.amenity_ids:
                amenities_list.append(amenities)
        return amenities_list

    # Setter task 10
    @amenities.setter
    def amenities(self, amenity):
        from models.amenity import Amenity
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
