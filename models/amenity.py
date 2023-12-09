#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Table, ForeignKey

# Assuming 'place_amenity' is a Table representing the many-to-many relationship
# between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True))


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
        place_amenities: relationship with Place through the 'place_amenity' association table
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = ""

    def to_dict(self):
        """Return a dictionary representation of Amenity"""
        amenity_dict = super().to_dict()
        amenity_dict['name'] = self.name
        return amenity_dict

    def __str__(self):
        """Return the string representation of Amenity"""
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)
