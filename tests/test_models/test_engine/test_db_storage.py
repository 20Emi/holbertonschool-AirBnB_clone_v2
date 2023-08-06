#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
import os
import subprocess
import MySQLdb


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    @classmethod
    def setUpClass(cls):
        # Set up the database connection for testing
        cls.db = MySQLdb.connect(
            host='localhost',
            user='hbnb_dev',
            passwd='hbnb_dev_pwd',
            db='hbnb_dev_db'
        )
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.db.close()

    def setUp(self):
        # Clean up the database before each test
        # self.cursor.execute("DELETE FROM cities")
        # self.cursor.execute("DELETE FROM states")
        self.db.commit()

    def test_create_state(self):
        # Test creating a new state in the database
        cmd = (
            'echo \'create State name="Utah"\' | HBNB_MYSQL_USER=hbnb_dev '
            'HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost '
            'HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py'
        )
        subprocess.run(cmd, shell=True)

        self.cursor.execute("SELECT * FROM states")
        states = self.cursor.fetchall()
        self.assertEqual(len(states), 1)
        state_data = states[0]
        self.assertEqual(state_data[2], 'Utah')


if __name__ == '__main__':
    unittest.main()
