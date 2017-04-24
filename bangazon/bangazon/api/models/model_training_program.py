"""
bangazon api model Configuration for product type
"""

from django.db import models

class TrainingProgram(models.Model):
    '''This class represents a product type that defines one data fields.
     
    Data Fields: 
        name [Refers to the name of the training program]
        startdate [Refers to the program's start date]
        enddate [Refers to the program's end date]
        maxenrollment [Refers to the maximum number of enrollee's for the program]

    Author:
        Adam Myers
    '''
    name = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()
    maxenrollment = models.SmallIntegerField()