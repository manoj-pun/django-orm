from orm_core.models import Restaurant, StaffRestaurant, Staff,Rating,Sale
from django.db.models import Avg, Count
from django.db import connection
from django.db.models import F
import random
from datetime import date

def run():
    restaurant, created = Restaurant.objects.get_or_create(
        name="Pizzeria 5",
        defaults={
            'date_opened': date.today(),
            'latitude': 40.7128,
            'longitude': -74.0060,
            'restaurant_type': 'IT'
        }
    )

    print(created)
    print(restaurant.id)



