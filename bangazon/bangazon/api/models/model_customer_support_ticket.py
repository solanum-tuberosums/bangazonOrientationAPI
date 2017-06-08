"""
bangazon api model configuration for customer support ticket
"""

from django.db import models
from bangazon.api.models import *
from django.contrib.auth.models import User


class CustomerSupportTicket(models.Model):
    """
    This class models a customer support ticket in the API's database.

    ----Fields----
    customer_id(foreign key): refers to the Customer(CustomerID) the support ticket is assigned to with a foreign key
    ticket_description(character): description of what the ticket is about
    order_id(foreign key): refers to the Order(OrderID) the ticket is associated with
    date_created(date): the date a ticket was added to the database
    resolution_description(character): description of how to resolve the ticket
    date_resolved(date): the date a ticket was resolved

    Author: Adam Myers
    """

    customer_id = models.ForeignKey(User)
    ticket_description = models.CharField(max_length=200)
    order_id = models.ForeignKey(Order)
    date_created = models.DateField()
    resolution_description = models.CharField(max_length=200, blank=True, null=True)
    date_resolved = models.DateField(blank=True, null=True)