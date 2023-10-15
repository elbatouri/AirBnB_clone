#!/usr/bin/python3
"""
a unittest for the console
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class test_console(unittest.TestCase):
    """ class to testout HBNBC command """
    def setUp(self):
        """creates an instance of HBNBCommand before each test"""
        self.cli = HBNBCommand()

    def test_create(self):
        """ checks the behavior of the create command when
            provided with different inputs"""
        return HBNBCommand()

    def test_EOF(self):
        """ tests the behavior of EOF command """
        self.assertTrue(self.cli.onecmd("EOF"))

    def test_quit(self):
        """ tests the quit command on the console """
        self.assertTrue(self.cli.onecmd("quit"))


if __name__ == '__main__':
    unittest.main()
