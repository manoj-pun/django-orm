from orm_core.models import Restaurant, StaffRestaurant, Staff,Rating,Sale
from django.db.models import Avg, Count
from django.db import connection
from django.db.models import F, Subquery, OuterRef
import random
from datetime import date
from django.db.models.functions import Upper,Length

def run():

    # latest_sale_income = Sale.objects.filter(
    # restaurant=OuterRef('pk')  # Reference the outer query's restaurant
    # ).order_by('-datetime').values('income')[:1]  # Take only the first/latest

    # # Main query with subquery
    # restaurants = Restaurant.objects.annotate(
    #     latest_income=Subquery(latest_sale_income)
    # )



    # for restaurant in restaurants:
    #     print(f"{restaurant.name}: Latest sale = {restaurant.latest_income}")


    restaurant = Restaurant.objects.annotate()

    for r in restaurant:
        print(r.name)



