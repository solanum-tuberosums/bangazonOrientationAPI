"""
bangazon api model configuration for product type
"""

from django.db import models


class ProductType(models.Model):
    """
    This class models a product type in the API's database. 

    ----Fields---- 
    label(character): the name of the product type

    Author: Adam Myers
    """
    
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title