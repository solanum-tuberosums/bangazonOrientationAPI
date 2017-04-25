"""
bangazon api model configuration for training program
"""

from django.db import models

class TrainingProgram(models.Model):
    """
    This class models a training program in the API's database. 

    ----Fields---- 
    name(character): the name of the training program
    start_date(date): the program's start date
    end_date(date): the program's end date
    max_enrollment(small integer): the maximum number of enrollee's for the program

    Author: Adam Myers
    """
    
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    max_enrollment = models.SmallIntegerField()

    def __str__(self):
        return self.name