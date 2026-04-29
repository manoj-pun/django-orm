from django.shortcuts import render, redirect
from .forms import RatingForm

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
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("index")  

    else:
        form = RatingForm()

    return render(request, "orm_core/index.html", {"form": form})