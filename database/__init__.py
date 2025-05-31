import os
from .models.turtle import *
from mongoengine import connect


def connect_to_db():
    """Connect to the MongoDB database using the URI from environment variables."""
    connect(
        host=os.getenv("MONGODB_URI", "mongodb://localhost:27017/python-discord-bot")
    )
