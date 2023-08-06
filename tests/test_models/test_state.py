#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test that the name attribute is set correctly"""
        name_value = "California"
        new = self.value(name=name_value)
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, name_value)
