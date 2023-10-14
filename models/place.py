#!/usr/bin/python3
"""Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place attributes:
        city_id (str): City's unique identifier.
        user_id (str): User's unique identifier.
        name (str): place's name.
        description (str): Place's the description.
        number_rooms (int): Rooms number.
        number_bathrooms (int): Bathrooms number.
        max_guest (int): guest Max capacity.
        price_by_night (int): Night's price.
        latitude (float): The place's latitude.
        longitude (float): The Place's longitude.
        amenity_ids (list): Amenities list.
    """

    city_id = ""
    ser_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
