#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City attributes:
        state_id (str) : State unique identifier
        name (str) : the name of the city

    """
    state_id = ""
    name = ""

