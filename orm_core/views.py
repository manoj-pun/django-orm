from django.shortcuts import render, redirect
from .forms import ProductOrderForm
from .models import Restaurant, Rating, Sale
from datetime import date
from django.db import transaction
from django.db import IntegrityError
from django.contrib import messages

def email_user():
    print(f"Dear user, Thank your for your order")

def index(request):
    restaurants = Restaurant.objects.all()
    
    for restaurant in restaurants:
        print(f"Restaurant: {restaurant.name}")
        print(f"Capacity: {restaurant.capacity}")
        print(f"Type: {restaurant.restaurant_type}")
        
        # Access related staff through StaffRestaurant
        staff_relations = restaurant.staffrestaurant_set.all()
        for staff_rel in staff_relations:
            print(f"  Staff: {staff_rel.staff.name}, Salary: {staff_rel.salary}")
    
    context = {
        'restaurants': restaurants
    }
    return render(request, "orm_core/index.html", context)

def order_product(request):
    if request.method == "POST":
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                order.product.number_in_stock -= order.number_of_items
                order.product.save()
            transaction.on_commit(email_user)
            return redirect("order_product")
        else:
            context = {"form":form}
            return render(request, "orm_core/order.html",context)
    form = ProductOrderForm()
    context = {"form":form}
    return render(request, "orm_core/order.html",context)

def create_rating(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        
        try:
            # Try to create the rating
            rating = Rating(
                user=request.user,
                restaurant=restaurant,
                rating=rating_value
            )
            rating.save()  # This will raise IntegrityError if invalid
            
            messages.success(request, 'Rating saved successfully!')
            return redirect('restaurant_detail', restaurant_id=restaurant_id)
            
        except IntegrityError as e:
            # Check if it's our rating constraint violation
            if 'rating_valid' in str(e):
                messages.error(request, 'Rating must be between 1 and 5!')
            else:
                messages.error(request, f'Database error: {e}')
            
            # Re-render the form with the attempted value
            return render(request, 'rate_restaurant.html', {
                'restaurant': restaurant,
                'attempted_rating': rating_value,
                'error': 'Rating must be between 1 and 5',
            })
    
    # GET request
    return render(request, 'rate_restaurant.html', {
        'restaurant': restaurant,
    })