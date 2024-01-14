#!/usr/bin/python3
"""
Module represents the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
