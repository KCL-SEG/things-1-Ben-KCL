
from django.db.models import Model

class Thing(Model):

    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
