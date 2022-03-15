#!/usr/bin/python3
'''test amenity'''

from datetime import datetime
from models.base_model import BaseModel
from datetime import datetime
import json
import unittest


class T_BaseModel(unittest.TestCase):
    '''test BaseModel class'''

    def test_meth(self):
        '''test method'''
        cls_test = BaseModel()
        self.assertEqual(type(cls_test.to_dict()), dict)

    def test_BaseModel_instantiation(self):
        """ test instantiation of BaseModel """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_BaseModel_instantiation_no_args(self):
        """ test instantiation of BaseModel with no args """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_BaseModel_instantiation_kwargs(self):
        """ test instantiation of BaseModel with kwargs """
        bm = BaseModel(name="bond")
        self.assertTrue(hasattr(bm, "name"))

    def test_BaseModel_created_date(self):
        """ test created_at """
        bm = BaseModel()
        self.assertTrue(isinstance(bm.created_at, datetime))

    def test_BaseModel_created_date2(self):
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime)

    def test_BaseModel_updated_date(self):
        """ test updated_at """
        bm = BaseModel()
        self.assertTrue(isinstance(bm.updated_at, datetime))

    def test_BaseModel_updated_date2(self):
        bm = BaseModel()
        self.assertEqual(type(bm.updated_at), datetime)

    def test_baseModel_save(self):
        test_save.save()


if __name__ == '__main__':
    unittest.main()
