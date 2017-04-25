"""
bangazon api model configuration for order-product
"""

from django.db import models
from bangazon.api.models import *


class OrderProduct(models.Model):

	"""
	This class models the relationship between the Order and Product resources in the API's database.  

	----Fields----
	product_id(foreign key): Links to Product(ProductID) with a foreign key
	order_id(foreign key): Links to Order(OrderID) with a foreign key

	Author: Jeremy Bakker
	"""

	product_id = models.ForeignKey(Product)
	order_id = models.ForeignKey(Order)