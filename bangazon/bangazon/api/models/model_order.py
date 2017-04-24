"""
bangazon api model configuration for order
"""

from django.db import models
from django.core.validators import MaxLengthValidator
from bangazon.api.models.model_customer import Customer


class Order(models.Model):

	"""This class represents a customer order and defines three data fields. 

	Data Fields: 
		PaymentTypeID [Refers to PaymentType(PaymentTypeID) without a foreign key]
		OrderDate
		CustomerID [Links to Customer(CustomerID) with a foreign key]

	Author: Jeremy Bakker
	"""

	PaymentTypeID = models.DecimalField(max_digits = 20, decimal_places = 0)
	OrderDate = models.DateField()
	CustomerID = models.ForeignKey(Customer)


