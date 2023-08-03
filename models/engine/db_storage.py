#!/usr/bin/python3
"""comment"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor. Set up the DB connection"""
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """comment"""
        pass

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        # self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """*create all tables in the database
        *reate the current database session"""
        Base.metadata.create_all(self.__engine)

        # crea una funcion de fabrica de sisiones
        my_session = sessionmaker(self.__engine, expire_on_commit=False)

        # crea un objeto de secion
        Session = scoped_session(my_session)

        # my_session.close()
