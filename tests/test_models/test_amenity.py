#!/usr/bin/python3
"""
Unittests for Amenity class
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import unittest

storage_t = getenv("HBNB_TYPE_STORAGE")

class TestAmenity(test_basemodel):
    """Test Amenity class functionality"""

    def setUp(self):
        """Set up test instances"""
        super().setUp()
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after tests"""
        del self.amenity

    def test_name_type(self):
        """Test if the type of 'name' attribute is string"""
        self.assertEqual(type(self.amenity.name), str)

    def test_str_method(self):
        """Test __str__ method"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_default_name(self):
        """Test that the default value of 'name' is an empty string"""
        if storage_t == 'db':
            self.assertIsNone(self.amenity.name)
        else:
            self.assertEqual(self.amenity.name, "")

    def test_to_dict_method(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertFalse("_sa_instance_state" in amenity_dict)

    def test_to_dict_attributes(self):
        """Test that the attributes are in to_dict output"""
        amenity_dict = self.amenity.to_dict()
        for attr in self.amenity.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_user_id_and_createat(self):
        """Testing id and created_at for every Amenity instance"""
        amenity1 = Amenity()
        sleep(2)
        amenity2 = Amenity()
        sleep(2)
        amenity3 = Amenity()
        sleep(2)
        list_amenities = [amenity1, amenity2, amenity3]

        for instance in list_amenities:
            amenity_id = instance.id
            with self.subTest(amenity_id=amenity_id):
                self.assertIsInstance(amenity_id, str)

        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertNotEqual(amenity1.id, amenity3.id)
        self.assertNotEqual(amenity2.id, amenity3.id)

        self.assertTrue(amenity1.created_at <= amenity2.created_at)
        self.assertTrue(amenity2.created_at <= amenity3.created_at)
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)
        self.assertNotEqual(amenity1.created_at, amenity3.created_at)
        self.assertNotEqual(amenity3.created_at, amenity2.created_at)

    def test_str_method(self):
        """Test __str__ method"""
        amenity = Amenity()
        str_output = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str_output, str(amenity))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it updates"""
        amenity = Amenity()
        created_at = amenity.created_at
        sleep(2)
        updated_at = amenity.updated_at
        amenity.save()
        new_created_at = amenity.created_at
        sleep(2)
        new_updated_at = amenity.updated_at

        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

class TestPEP8(unittest.TestCase):
    """Test PEP8 compliance"""

    def test_pep8_style(self):
        """Check PEP8 style for Amenity module"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

class TestAmenityInheritance(unittest.TestCase):
    """Test Amenity class inheritance"""

    def test_instance(self):
        """Check if Amenity is an instance of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")

    def test_id_creation(self):
        """Test that unique ids are created for each Amenity instance"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_created_at(self):
        """Test that created_at is a valid datetime object"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at is a valid datetime object"""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)


class TestAmenityAdditional(unittest.TestCase):
    """Additional test cases for Amenity class"""

    def test_name_attr(self):
        """Test that Amenity has attribute 'name', and it's an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_t == 'db':
            self.assertIsNone(amenity.name)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        amenity = Amenity()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)
        self.assertEqual(amenity_dict["created_at"], amenity.created_at.strftime(t_format))
        self.assertEqual(amenity_dict["updated_at"], amenity.updated_at.strftime(t_format))

if __name__ == '__main__':
    unittest.main()
