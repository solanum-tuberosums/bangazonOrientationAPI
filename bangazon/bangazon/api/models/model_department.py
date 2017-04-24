from django.db import models


class Department(models.Model):
    """
    This class models a department in the API's database.

    ----Fields----
    name(string): the name of the department
    budget(decimal): the budget of the department

    Author: Jeremy Bakker
    """

    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.name