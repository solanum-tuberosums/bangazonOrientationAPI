from django.db import models

from bangazon.api.models import ProductType, Customer

"""
This class represents a Product:
    - Author: Will Sims
    - Purpose: to track Bangazon's products
    - Data Fields (5):
        Price:          price of an individual product
        Title:          the name/title of the product
        Description:    description of the product
        ProductTypeId:  id of the type category that the product belongs to
        CustomerId:     id of the customer who created/posted the product

"""


class Product(models.Model):
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Title = models.CharField(max_length=40)
    Description = models.TextField(max_length=256)
    ProductType = models.ForeignKey(ProductType)
    Customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.Title





