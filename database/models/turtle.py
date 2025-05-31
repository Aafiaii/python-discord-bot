from mongoengine import Document, StringField


class Turtle(Document):
    name = StringField(required=True)
