"""
bangazon api model configuration for the employee-computer joining table
"""

from django.db import models
from bangazon.api.models import *


class EmployeeComputer(models.Model):
    """
    This class models the relationship between the Employee and Computer
    resources in the API's database.

    ----Fields----
    date_assigned(date): the date the department was assigned
    employee_id(foreign key): the employee to whom the computer was assigned to
    computer_id(foreign key): the computer being assigned

    Author: Zak Spence
    """

    date_assigned = models.DateField()
    employee_id = models.ForeignKey(Employee)
    computer_id = models.ForeignKey(Computer)