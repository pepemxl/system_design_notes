from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Product

from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


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
    
class PaymentProcessView(TemplateView):
    template_name = 'payment_process.html'

    def post(self, request, *args, **kwargs):
        token = request.POST.get('stripeToken')

        try:
            charge = stripe.Charge.create(
                amount=1000,  # Monto en centavos
                currency='usd',
                source=token,
                description='Payment for Order #123'
            )
            # TODO: 
            # - crear una orden en base de datos,
            # - enviar un correo electrónico de confirmación,
            # - enviar a servicio de trackeo de operacion
            # return self.render_to_response({'success': True})
            return redirect('payment_confirmation')
        except stripe.error.CardError as e:
            error_message = e.error.message
            return self.render_to_response({'error': error_message})
        except Exception as e:
            error_message = str(e)
            return self.render_to_response({'error': error_message})    
    


class PaymentConfirmationView(View):
    def get(self, request):
        return render(request, 'store/payment_confirmation.html')
