#!/usr/bin/env python3
"""
Unitest for models/city.py

Unittest classes:
    Test_city_instantiation
    """
import os
import unittest
import models
from datetime import datetime
from models.amenity import Amenity
from time import sleep


class Test_models_city(unittest.TestCase):
    """
        Test_models_city class
    """

    def test_instantiation_no_args(self):
        self.assertEqual(City, type(City()))

    def test_args_unused(self):
        city1 = City(None)
        self.assertNotIn(None, city1.__dict__.values())

    def test_instantiation_kwargs(self):
        am_date = datetime.today()
        dt_iso = am_date.isoformat()
        city1 = City(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city1.id, "123")
        self.assertEqual(city1.created_at, am_date)
        self.assertEqual(city1.updated_at, am_date)

    def test_instantiation_kwargs_none(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_instantiation_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_public_class_attr(self):
        city1 = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(City()))
        self.assertNotIn("name", city1.__dict__)

    def test_twocity_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_city_created_at(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertLess(amen1.created_at, amen2.created_at)

    def test_two_amenities_updated_at(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_city_str(self):
        am_date = datetime.today()
        dt_repr = repr(am_date)
        city1 = City()
        city1.id = "121212"
        city1.created_at = city1.updated_at = am_date
        amstr = city1.__str__()
        self.assertIn("[City] (121212)", amstr)
        self.assertIn("'id': '121212'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

     def test_args_unused(self):
        city1 = City(None)
        self.assertNotIn(None, city1.__dict__.values())


if __name__ == '__main__':
    unittest.main()
