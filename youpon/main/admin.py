from django.contrib import admin
from .models import List, Item, Coupon

# Register your models here.
admin.site.register(List)
admin.site.register(Item)
admin.site.register(Coupon)