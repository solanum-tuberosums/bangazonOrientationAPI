"""
bangazon api model configuration for payment type
"""
from django.db import models
from bangazon.api.models.model_customer import Customer

# Create your models here.
class PaymentType(models.Model):
	'''This class represents our payment type resource defines 4 data fields.

	DataFields:
		accountLabel
		accountType
		accountNumber
		customerID [Links to Customer(CustomerID) with a foregin key]

	Author: Blaise Roberts	
	'''
	accountLabel = models.CharField(max_length=20)
	accountType = models.CharField(max_length=20)
	accountNumber = models.DecimalField(max_digits=20, decimal_places=0)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	def __str__(self):
		return self.accountLabel
	