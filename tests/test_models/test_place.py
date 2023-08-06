#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test that the city_id attribute is set correctly"""
        city_id_value = "city123"
        new = self.value(city_id=city_id_value)
        self.assertEqual(type(new.city_id), str)
        self.assertEqual(new.city_id, city_id_value)

    def test_user_id(self):
        """Test that the user_id attribute is set correctly"""
        user_id_value = "user123"
        new = self.value(user_id=user_id_value)
        self.assertEqual(type(new.user_id), str)
        self.assertEqual(new.user_id, user_id_value)

    def test_name(self):
        """Test that the name attribute is set correctly"""
        name_value = "Los Angeles"
        new = self.value(name=name_value)
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, name_value)

    def test_description(self):
        """Test that the description attribute is set correctly"""
        description_value = "A beautiful city"
        new = self.value(description=description_value)
        self.assertEqual(type(new.description), str)
        self.assertEqual(new.description, description_value)

    def test_number_rooms(self):
        """Test that the number_rooms attribute is set correctly"""
        number_rooms_value = 3
        new = self.value(number_rooms=number_rooms_value)
        self.assertEqual(type(new.number_rooms), int)
        self.assertEqual(new.number_rooms, number_rooms_value)

    def test_number_bathrooms(self):
        """Test that the number_bathrooms attribute is set correctly"""
        number_bathrooms_value = 2
        new = self.value(number_bathrooms=number_bathrooms_value)
        self.assertEqual(type(new.number_bathrooms), int)
        self.assertEqual(new.number_bathrooms, number_bathrooms_value)

    def test_max_guest(self):
        """Test that the max_guest attribute is set correctly"""
        max_guest_value = 5
        new = self.value(max_guest=max_guest_value)
        self.assertEqual(type(new.max_guest), int)
        self.assertEqual(new.max_guest, max_guest_value)

    def test_price_by_night(self):
        """Test that the price_by_night attribute is set correctly"""
        price_by_night_value = 100
        new = self.value(price_by_night=price_by_night_value)
        self.assertEqual(type(new.price_by_night), int)
        self.assertEqual(new.price_by_night, price_by_night_value)

    def test_latitude(self):
        """Test that the latitude attribute is set correctly"""
        latitude_value = 37.7749
        new = self.value(latitude=latitude_value)
        self.assertEqual(type(new.latitude), float)
        self.assertEqual(new.latitude, latitude_value)

    def test_longitude(self):
        """Test that the longitude attribute is set correctly"""
        longitude_value = -122.4194
        new = self.value(longitude=longitude_value)
        self.assertEqual(type(new.longitude), float)
        self.assertEqual(new.longitude, longitude_value)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
