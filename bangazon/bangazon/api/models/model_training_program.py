"""
bangazon api model Configuration for training program
"""

from django.db import models

class TrainingProgram(models.Model):
    '''This class represents a training program that defines one data fields.
     
    Data Fields: 
        name [Refers to the name of the training program]
        startdate [Refers to the program's start date]
        enddate [Refers to the program's end date]
        maxenrollment [Refers to the maximum number of enrollee's for the program]

    Author:
        Adam Myers
    '''
    Name = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()
    MaxEnrollment = models.SmallIntegerField()

    def __str__(self):
        """ Retrieves the value of Name

        Arguments:
            n/a
        """
        return self.Name