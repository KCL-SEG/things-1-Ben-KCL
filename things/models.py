
from django.db.models import Model

class Thing(Model):

    def __init__(self, name, description, quantity):
        super().__init__()
        self.name = name
        self.description = description
        self.quantity = quantity
