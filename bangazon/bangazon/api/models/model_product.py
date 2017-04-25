"""
bangazon api model configuration for product
"""

from django.db import models
from bangazon.api.models import *


class Product(models.Model):
    """
    This class models a product in the API's database. 

    ----Fields---- 
    price(decimal: price of an individual product
    title(character): the name/title of the product
    description(text): description of the product
    product_type(foreign key): id of the type category that the product belongs to
    customer(foreign key): id of the customer who created/posted the product

    Author: Will Sims
    """

    price = models.DecimalField(decimal_places=2, max_digits=10)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=256)
    product_type = models.ForeignKey(ProductType)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.title