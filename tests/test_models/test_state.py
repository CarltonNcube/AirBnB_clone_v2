#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Test State class functionality"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test if the type of 'name' attribute is string"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        state = State(name="California")
        state_dict = state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "California")

    def test_str_method(self):
        """Test __str__ method"""
        state = State(name="New York")
        str_output = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str_output, str(state))

    def test_places_relationship(self):
        """Test the places relationship"""
        state = State(name="Texas")
        state.save()

        # Create a Place associated with the State
        place_attrs = {"name": "Awesome Place", "state_id": state.id}
        place = self.value(**place_attrs)
        place.save()

        # Refresh the state to get the updated places relationship
        self.value.storage.reload()
        refreshed_state = self.value.get(state.id)

        # Check if the place is in the places relationship
        self.assertIn(place, refreshed_state.places)

    # Add more test methods for other functionalities...

if __name__ == '__main__':
    unittest.main()
