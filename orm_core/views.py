from django.shortcuts import render, redirect
from .forms import RatingForm
from .models import Restaurant, Rating, Sale

# def index(request):
#     if request.method == "POST":
#         form = RestaurantForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return redirect("index")  

#     else:
#         form = RestaurantForm()

#     return render(request, "orm_core/index.html", {"form": form})


def index(request):
    ratings = Rating.objects.select_related("restaurant")
    context = {"ratings":ratings}

    return render(request, "orm_core/index.html", context)