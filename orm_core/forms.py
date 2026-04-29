from django import forms
from .models import Rating,Restaurant
from django.core.validators import MinValueValidator,MaxValueValidator

# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ("restaurant","user","rating")


# class RestaurantForm(forms.ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = ("name","restaurant_type")


class RatingForm(forms.Form):
    rating = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
