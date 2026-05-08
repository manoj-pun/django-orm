from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        NEPALESE = 'NE', "Nepalese"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        OTHER = "OT", "Other"

    name = models.CharField(max_length=100)
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
    capacity = models.PositiveSmallIntegerField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        print(self._state.adding,flush=True)
        super().save(*args,**kwargs)

class Staff(models.Model):
    name = models.CharField(max_length=128)
    restaurants = models.ManyToManyField(Restaurant,through="StaffRestaurant")


class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    salary = models.FloatField(null=True)
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name="ratings")
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return f"Rating: {self.rating}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="rating_value_valid",
                condition=Q(rating__gte=1,rating__lte=5),
                violation_error_message="Rating invalid:must fall between 1 and 5",
            ),
            models.UniqueConstraint(
                fields=["user","restaurant"],
                name="user_restaurant_uniq",
            )
        ]
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True,related_name="sales")
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    number_in_stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.number_of_items} x {self.product.name}"
