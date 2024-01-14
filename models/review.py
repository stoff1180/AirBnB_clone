#!/usr/bin/python3
"""
Module represents the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
