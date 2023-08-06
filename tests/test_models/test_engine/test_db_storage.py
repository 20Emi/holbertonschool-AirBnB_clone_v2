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
    """Class to test the DB storage method"""

    @classmethod
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def setUpClass(cls):
        """Set up the test environment"""
        cls.storage = DBStorage()
        cls.storage.reload()  # Load data from the database

    @classmethod
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def tearDownClass(cls):
        """Tear down the test environment"""
        cls.storage._DBStorage__session.close()  # Close the database session

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def test_new_user(self):
        # Create a new User instance with a valid email and password
        user = User(email='user1@example.com', password='password1')
        self.storage.new(user)
        self.assertIn(user, self.storage._DBStorage__session.new)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Skip")
    def test_save_user(self):
        user = User(email='user2@example.com', password='password2')
        self.storage.new(user)
        self.storage.save()
        self.assertIn(user, self.storage._DBStorage__session)


if __name__ == '__main__':
    unittest.main()
