#!/usr/bin/python3
"""review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review attributes:
        place_id (str): place unique identifier
        user_id (str): user unique identifier
        text_id (str): the content of the review
    """
    place_id = ""
    user_id = ""
    text_id = ""
