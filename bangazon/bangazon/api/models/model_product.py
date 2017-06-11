"""
bangazon api model configuration for product
"""

from django.db import models
from bangazon.api.models import *


class Product(models.Model):
    """
    This class models a product in the API's database. 

    ----Fields---- 
    price(decimal): price of an individual product
    title(character): the name/title of the product
    description(text): description of the product
    product_type(foreign key): links to ProductType(ProductTypeID) with a foregin key
    customer(foreign key): links to Customer(CustomerId) with a foreign key

    Author: Will Sims
    """

    price = models.DecimalField(decimal_places=2, max_digits=10)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=256)
    product_type = models.ForeignKey(ProductType, null=True)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.title
