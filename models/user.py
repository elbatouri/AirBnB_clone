#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class of the user

    user's attributes:
        email (str): email address
        password (str): user's password
        first_name (str) : user's first Name
        last_name (str) : user's last Name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
