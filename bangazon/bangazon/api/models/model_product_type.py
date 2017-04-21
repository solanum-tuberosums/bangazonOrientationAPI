from django.db import models

# Create your models here.
class ProductType(models.Model):
	label = models.CharField(max_length=50)

	def __str__(self):
		return self.label
