"""
bangazon api model configuration for payment type
"""

from django.db import models
from bangazon.api.models import *


class PaymentType(models.Model):
	"""
	This class models a payment type in the API's database. 

    ----Fields---- 
	account_label(character): name of payment 
	account_type(character): type of payment
	account_number(decimal): account number
	customer_id(foreign key): links to Customer(CustomerID) with a foregin key

	Author: Blaise Roberts	
	"""
	
	account_label = models.CharField(max_length=20)
	account_type = models.CharField(max_length=20)
	account_number = models.DecimalField(max_digits=20, decimal_places=0)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return self.account_label	