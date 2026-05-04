from orm_core.models import Restaurant, StaffRestaurant, Staff,Rating,Sale
from django.db.models import Avg, Count
from django.db import connection
from django.db.models import F
import random

def run():
    restaurants = Restaurant.objects.annotate(rating_count=Count('ratings'))

    for restaurant in restaurants:
        print(f"{restaurant.name}: {restaurant.rating_count} ratings")

