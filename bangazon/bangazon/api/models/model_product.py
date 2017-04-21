from django.db import models


class Product(models.Model):
    Price = models.DecimalField(decimal_places=2)
    Title = models.CharField(max_length=40)
    Description = models.TextField(max_length=255)
    # ProductTypeId = models.ForeignKey(ProductType)
    # CustomerId = models.ForeignKey(Customer)







