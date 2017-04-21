"""
bangazon api model configuration for order
"""

from django.db import models

class Order(models.Model):

	"""This class represents a customer order and defines three data fields. 

	Data Fields: 
		PaymentTypeID [Refers to PaymentType(PaymentTypeID) without a foreign key]
		OrderDate
		CustomerID [Links to Customer(CustomerID) with a foreign key]

	Author: Jeremy Bakker
	"""

	PaymentTypeID = models.BigIntegerField()
	OrderDate = models.DateField()
	# CustomerID = models.ForeignKey(Customer)


