from django.db import models

# Create your models here.
class PaymentType(models.Model):
	'''This class represents our payment type resource and have 4 data fields.

	DataFields:
		accountLabel
		accountType
		accountNumber
		customerID [Links to Customer(CustomerID) with a foregin key]
	'''
	accountLabel = models.CharField(max_length=20)
	accountType = models.CharField(max_length=20)
	accountNumber = models.BigIntegerField()
	# customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
	def __str__(self):
		return self.accountLabel
	