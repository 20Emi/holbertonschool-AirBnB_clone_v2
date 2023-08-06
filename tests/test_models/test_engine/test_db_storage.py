#!/usr/bin/python3
"""unnitest of db_storage"""
import models
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import unittest
import MySQLdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
from models import storage


class test_DB_Storage(unittest.TestCase):
    """tests"""

    @classmethod
    def up(self):
        """se esta configurando de la base de datos de prueba
        y la sesion"""
        if isinstance(models.storage, DBStorage):
            Base.metadata.create_all(self.storage.__DBStorage__engine)
            Session = sessionmaker(self.storage.__DBStorage__engine)
            self.storage._DBStorage__session = self.Session()
            self.amenity = Amenity(name='EC')
            self.storage._DBStorage__session.add(self.amenity)

            self.city = City(name='EC', state_id=self.state.id)
            self.storage._DBStorage__session.add(self.city)

            self.place = Place(
                name='EC', city_id=self.city.id, user_id=self.user.id)
            self.storage._DBStorage__session.add(self.place)

            self.review = Review(
                text='hola mundo', place_id=self.place.id, user_id=self.user.id)
            self.storage._DBStorage__session.add(self.review)

            self.user = User(email='ec@gmail.com', password='root')
            self.storage._DBStorage__session.add(self.user)

            self.state = State(name='EC')
            self.storage._DBStorage__session.add(self.state)

    def down(self):
        self.storage._DBStorage__session.close()

    def test_new(self):
        user = User()
        self.storage.new(user)
        self.assertIn(user, self.storage._DBStorage__session.new)

    def test_save(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.assertIn(user, self.storage._DBStorage__session)
