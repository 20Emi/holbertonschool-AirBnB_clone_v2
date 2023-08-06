#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test that the place_id attribute is set correctly"""
        place_id_value = "place123"
        new = self.value(place_id=place_id_value)
        self.assertEqual(type(new.place_id), str)
        self.assertEqual(new.place_id, place_id_value)

    def test_user_id(self):
        """Test that the user_id attribute is set correctly"""
        user_id_value = "user123"
        new = self.value(user_id=user_id_value)
        self.assertEqual(type(new.user_id), str)
        self.assertEqual(new.user_id, user_id_value)

    def test_text(self):
        """Test that the text attribute is set correctly"""
        text_value = "This is a review."
        new = self.value(text=text_value)
        self.assertEqual(type(new.text), str)
        self.assertEqual(new.text, text_value)
