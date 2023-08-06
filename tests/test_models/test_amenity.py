#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test that the name attribute is set correctly"""
        name_value = "Place Name"
        new = self.value(name=name_value)
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, name_value)
