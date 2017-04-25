"""
bangazon api model configuration for employee
"""

from django.db import models
from bangazon.api.models import *


class Employee(models.Model):
    """
    This class models an employee in the API's database. 

    ----Fields---- 
    first_name(character): the first name of the employee
    last_name(character): the last name of the employee
    is_supervisor(integer): defines whether an employee is a supervisor (0 for False, 1 for True)
    department_id(foreign key): refers to the Department(DepartmentID) the employee is assigned to with a foreign key

    Author: Adam Myers
    """
    
    options = (
        (0, 'False'),
        (1, 'True'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_supervisor = models.IntegerField(default=0, choices=options)
    department_id = models.ForeignKey(Department)