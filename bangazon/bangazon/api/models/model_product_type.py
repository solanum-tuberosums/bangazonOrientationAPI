"""
bangazon api model Configuration for product type
"""

from django.db import models

class ProductType(models.Model):
    '''This class represents a product type that defines one data fields. 

    Data Fields: 
        label [Refers to the name of the product type.]

    Author:
        Adam Myers
    '''
    label = models.CharField(max_length=50)

    def __str__(self):
        """ Retrieves the value of label

        Arguments:
            n/a
        """
        return self.label
