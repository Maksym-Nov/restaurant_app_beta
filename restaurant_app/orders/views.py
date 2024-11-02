# orders/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from menu.models import Dish

def cart(request):
    # Ініціалізація кошика
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for item_id, quantity in cart.items():
        dish = Dish.objects.get(id=item_id)
        cart_items.append({
            'dish': dish,
            'quantity': quantity,
            'total_price': dish.price * quantity,
        })
        total_price += dish.price * quantity
    return render(request, 'orders/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, id):
    # Додавання в кошик
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    # Оформлення замовлення
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=0)
        total_price = 0
        for item_id, quantity in cart.items():
            dish = Dish.objects.get(id=item_id)
            OrderItem.objects.create(order=order, dish=dish, quantity=quantity)
            total_price += dish.price * quantity
        order.total_price = total_price
        order.save()
        request.session['cart'] = {}  # Очищення кошика
        return redirect('order_history')
    return render(request, 'orders/checkout.html')

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
