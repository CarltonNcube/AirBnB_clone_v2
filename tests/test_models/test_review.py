#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Test Review class functionality"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """Test if the type of 'place_id' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id_type(self):
        """Test if the type of 'user_id' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text_type(self):
        """Test if the type of 'text' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        review = Review(place_id="123", user_id="456", text="Nice place!")
        review_dict = review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)

    def test_str_method(self):
        """Test __str__ method"""
        review = Review(place_id="789", user_id="101", text="Great experience!")
        str_output = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str_output, str(review))

if __name__ == '__main__':
    unittest.main()
