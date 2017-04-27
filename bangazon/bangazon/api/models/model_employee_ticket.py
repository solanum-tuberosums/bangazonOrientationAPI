"""
bangazon api model configuration for the employee-customer_support_ticket joining table
"""

from django.db import models
from bangazon.api.models import *


class EmployeeTicket(models.Model):
    """
    This class models the relationship between the Employee and Customer Support Ticket resources in the API's database.

    ----Fields----
    employee_id(foreign key): links to Employee(EmployeeID) with a foregin key
    customer_support_ticket_id(foreign key): links to CustomerSupportTicket(CustomerSupportTicketID) with a foregin key

    Author: Adam Myers
    """

    employee_id = models.ForeignKey(Employee)
    customer_support_ticket_id = models.ForeignKey(CustomerSupportTicket)