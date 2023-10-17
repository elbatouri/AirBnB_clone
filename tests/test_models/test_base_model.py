#!/usr/bin/python3
""" imorts modules to test base_model class"""
import unittest
import json
import pep8
from time import sleep

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """The class in which the basemodel will be tested"""
    def test_doc_module(self):
        "Test length of doc"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """tests the constructor '__init__'"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """Tests object creation and to_dict method"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "airbnb"
        my_model.my_number = 2008
        self.assertEqual(my_model.name, "airbnb")
        self.assertEqual(my_model.my_number, 2008)
        attr_types_json = {
                "my_number": int,
                "name": str,
                "__class__": str,
                "id": str,
                "created_at": str,
                "updated_at": str,
        }
        my_model_json = my_model.to_dict()
        for key, value in attr_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_file_save(self):
        """Test file save function"""
        bmo = BaseModel()
        bmo.save()
        with open("file.json", 'r') as f:
            self.assertIn(bmo.id, f.read())


if __name__ == '__main__':
    unittest.main()
