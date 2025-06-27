from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class List(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="list", null=True)
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    list = models.ForeignKey(List, on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Coupon(models.Model):
    store = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    discount = models.FloatField()
    discount_type = models.CharField(max_length=20, choices=[('percent', 'Percent'), ('bogo', 'Buy-One-Get-One-Free'), ('fixed', 'Fixed Amount')])
    expiration_date = models.DateField()

    def __str__(self):
        return (
            f"Store: {self.store}\n"
            f"Item: {self.item}\n"
            f"Discount: {self.discount} ({self.discount_type})"
        )