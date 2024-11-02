from django.shortcuts import render, get_object_or_404
from .models import Dish

def menu_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu_list.html', {'dishes': dishes})

def dish_detail(request, id):
    dish = get_object_or_404(Dish, id=id)
    return render(request, 'menu/dish_detail.html', {'dish': dish})
