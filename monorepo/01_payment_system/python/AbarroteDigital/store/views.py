from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Product

from django.conf import settings

# Create your views here.

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'store/product_list.html', {'products': products})
    
    def product_list(request):
        products = Product.objects.all()
        return render(request, 'store/product_list.html', {'products': products})

class AddToCartView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        cart = request.session.get('cart', [])
        cart.append(product.id)
        request.session['cart'] = cart
        messages.success(request, 'Producto agregado al carrito.')
        return redirect('cart')

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', [])
        products = Product.objects.filter(id__in=cart)
        return render(request, 'store/cart.html', {'products': products})

class CheckoutView(View):
    def get(self, request):
        cart = request.session.get('cart', [])
        products = Product.objects.filter(id__in=cart)
        total_price = sum([product.price for product in products])
        return render(request, 'store/checkout.html', {'products': products, 'total_price': total_price})

class PaymentProcessView(View):
    def post(self, request):
        # Aquí testearemos los sistemas de pagi aqui agregaremos
        # la lógica para procesar el pago utilizando el servicio de pagos Visa
        messages.success(request, 'Pago procesado exitosamente.')
        return redirect('payment_confirmation')

class PaymentConfirmationView(View):
    def get(self, request):
        return render(request, 'store/payment_confirmation.html')
