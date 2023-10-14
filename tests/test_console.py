#!/usr/bin/python3
"""
a unittest for the console
"""
import unittest
from unittest.mock import patch
from io import StringIO
from your_module import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ class to testout HBNBC command """

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, cmd, expected_output, mock_stdout):
        """  captures the standard output and compares
             it with the expected output """
        with patch('builtins.input', return_value=cmd):
            HBNBCommand().onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create(self):
        """ checks the behavior of the create command when
            provided with different inputs"""
        self.assert_stdout("create BaseModel", "(hbnb) " + "\n")
        self.assert_stdout("create InvalidClass",
                           "(hbnb) ** class doesn't exist **\n")
        self.assert_stdout("create", "(hbnb) ** class name missing **\n")

    def test_show(self):
        """ checks the behavior of the show command
            when provided with different inputs """
        self.assert_stdout("show BaseModel",
                           "(hbnb) ** instance id missing **\n")
        self.assert_stdout("show BaseModel 123",
                           "(hbnb) ** no instance found **\n")
        self.assert_stdout("create BaseModel", "(hbnb) " + "\n")
        self.assert_stdout("show BaseModel 123",
                           "(hbnb) ** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
