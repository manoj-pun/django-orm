from orm_core.models import Restaurant, StaffRestaurant, Staff,Rating
from django.db.models import Avg

def run():
    print(Rating.objects.aggregate(average=Avg("rating"))) 