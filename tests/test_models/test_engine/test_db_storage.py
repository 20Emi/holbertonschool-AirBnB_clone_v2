#!/usr/bin/python3
"""unnitest of db_storage"""
from models.base_model import Base, BaseModel
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
from os import getenv


class test_DB_Storage(unittest.TestCase):
    """tests"""

    @classmethod
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def setUpClass(cls):
        """Set up the test environment"""
        cls.storage = DBStorage()
        cls.storage.reload()  # Load data from the database

    @classmethod
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def up(cls):
        """Set up the test environment"""
        if isinstance(models.storage, DBStorage):
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()

            # Create the User instance first
            cls.user = User(email='ec@gmail.com', password='root')
            cls.storage._DBStorage__session.add(cls.user)

            # Create other instances that depend on User
            cls.state = State(name='EC')
            cls.storage._DBStorage__session.add(cls.state)

            cls.amenity = Amenity(name='EC')
            cls.storage._DBStorage__session.add(cls.amenity)

            # Set cls.state.id before creating the City instance
            cls.city = City(name='EC', state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)

            # Set cls.user.id and cls.city.id before creating the Place
            cls.place = Place(
                name='EC', city_id=cls.city.id, user_id=cls.user.id)
            cls.storage._DBStorage__session.add(cls.place)

            # Set cls.place.id and cls.user.id before creating the Review
            cls.review = Review(
                text='hola', place_id=cls.place.id, user_id=cls.user.id)
            cls.storage._DBStorage__session.add(cls.review)

            cls.storage._DBStorage__session.commit()

    @classmethod
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def tearDownClass(cls):
        """Tear down the test environment"""
        cls.storage._DBStorage__session.close()  # Close the database session

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def test_new(self):
        # Create a new User instance with a valid email and password
        user = User(email='test@example.com', password='test')
        self.storage.new(user)
        self.assertIn(user, self.storage._DBStorage__session.new)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def test_save(self):
        user = User(email='test2@example.com', password='test2')
        self.storage.new(user)
        self.storage.save()
        self.assertIn(user, self.storage._DBStorage__session)


if __name__ == '__main__':
    unittest.main()
