"""
bangazon api model configuration for customer
"""

from django.db import models


class Customer(models.Model):
    """
    This class models a customer in the API's database.

    ----Fields----
    first_name(character): the first name of a customer
    last_name(character): the last name of a customer
    date_created(date): the date a user was added to the database

    Author: Zak Spence
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)