#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test that the first_name attribute is set correctly"""
        first_name_value = "John"
        new = self.value(first_name=first_name_value)
        self.assertEqual(type(new.first_name), str)
        self.assertEqual(new.first_name, first_name_value)

    def test_last_name(self):
        """Test that the last_name attribute is set correctly"""
        last_name_value = "Doe"
        new = self.value(last_name=last_name_value)
        self.assertEqual(type(new.last_name), str)
        self.assertEqual(new.last_name, last_name_value)

    def test_email(self):
        """Test that the email attribute is set correctly"""
        email_value = "john.doe@example.com"
        new = self.value(email=email_value)
        self.assertEqual(type(new.email), str)
        self.assertEqual(new.email, email_value)

    def test_password(self):
        """Test that the password attribute is set correctly"""
        password_value = "secretpassword"
        new = self.value(password=password_value)
        self.assertEqual(type(new.password), str)
        self.assertEqual(new.password, password_value)
