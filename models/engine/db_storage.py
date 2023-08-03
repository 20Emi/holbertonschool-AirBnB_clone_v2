#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import environ


class DBStorage():
    """This class manages storage of hbnb models in a MYSQL DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor. Set up the DB connection"""
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """Returns a dict depending of the class name"""
        print('All not completed yet')
        pass

    def new(self, obj):
        """Add an object to the database"""
        pass

    def save(self):
        """Commit all changes to the database"""
        pass

    def delete(self, obj=None):
        """Delete an object from the database"""
        pass

    def reload(self):
        """Create all tables in the database"""
        pass
