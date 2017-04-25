"""
bangazon api model configuration for the employee-training_program joining table
"""

from django.db import models
from bangazon.api.models import *


class EmployeeTraining(models.Model):
    """
    This class models the relationship between the Employee and Training Program resources in the API's database.

    ----Fields----
    training_id(foreign key): links to TrainingProgram(TrainingProgramID) with a foregin key
    employee_id(foreign key): links to Employee(EmployeeID) with a foregin key

    Author: Adam Myers
    """

    training_id = models.ForeignKey(TrainingProgram)
    employee_id = models.ForeignKey(Employee)