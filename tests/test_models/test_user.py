#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Test User class functionality"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """Test if the type of 'first_name' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name_type(self):
        """Test if the type of 'last_name' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email_type(self):
        """Test if the type of 'email' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password_type(self):
        """Test if the type of 'password' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        user = User(first_name="John", last_name="Doe", email="john@example.com", password="pass123")
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)

    def test_str_method(self):
        """Test __str__ method"""
        user = User(first_name="Alice", last_name="Wonderland", email="alice@example.com", password="pass456")
        str_output = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str_output, str(user))

if __name__ == '__main__':
    unittest.main()

