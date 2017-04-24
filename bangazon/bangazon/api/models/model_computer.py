from django.db import models


class Computer(models.Model):
    """
    This class models a computer in the API's database.

    ----Fields----
    date_purchased(date): date a computer was purchased by the company
    date_decommissioned(date): date a computer was decommissioned by the company

    Author: Zak Spence
    """
    date_purchased = models.DateField()
    date_decommissioned = models.DateField()
