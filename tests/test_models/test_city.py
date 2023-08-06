#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test that the state_id attribute is set correctly"""
        state_id_value = "state123"
        new = self.value(state_id=state_id_value)
        self.assertEqual(type(new.state_id), str)
        self.assertEqual(new.state_id, state_id_value)

    def test_name(self):
        """Test that the name attribute is set correctly"""
        name_value = "New York"
        new = self.value(name=name_value)  # Pass the name attribute
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, name_value)
