"""
bangazon api model Configuration for product type
"""

from django.db import models

class Employee(models.Model):
    '''This class represents a employee that defines three data fields. 

    Data Fields: 
        firstname [Refers to the name of the employee]
        lastname [Refers to the name of the employee]
        issupervisor [Refers to whether an employee is a supervisor (0 for no, 1 for no)]
        departmentid [Refers to the Department(DepartmentID) the employee is assigned to with a foreign key]

    Author:
        Adam Myers
    '''
    options = (
        (0, 'False'),
        (1, 'True'),
    )

    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    IsSupervisor = models.IntegerField(default=0, choices=options)
    #DepartmentID = models.ForeignKey(Department)


