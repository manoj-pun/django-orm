from django.shortcuts import render, redirect
from .forms import RatingForm
from .models import Restaurant, Rating, Sale
from datetime import date

# def index(request):
#     if request.method == "POST":
#         form = RestaurantForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return redirect("index")  

#     else:
#         form = RestaurantForm()

#     return render(request, "orm_core/index.html", {"form": form})


# def index(request):
#     ratings = Rating.objects.select_related("restaurant")
#     context = {"ratings":ratings}

#     return render(request, "orm_core/index.html", context)

def index(request):
    # Get or create one specific restaurant
    restaurant, created = Restaurant.objects.get_or_create(
        name="Pizzeria 1",
        defaults={
            'date_opened': date.today(),
            'latitude': 40.7128,
            'longitude': -74.0060,
            'restaurant_type': 'IT'
        }
    )
    
    # Get ALL restaurants to display
    restaurants = Restaurant.objects.all()  # ✅ Define the variable
    
    context = {"restaurants": restaurants}
    return render(request, "orm_core/index.html", context)