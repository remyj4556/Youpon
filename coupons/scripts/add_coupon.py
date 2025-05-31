# scripts/add_coupon.py

import sys
import os
import django
from datetime import date

# add base directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from coupons.models import Coupon

c = Coupon(
    store='Meijer',
    item='Cheese',
    discount='0.25',
    discount_type='percent',
    expiration_date=date(2025, 7, 5)
)
c.save()

