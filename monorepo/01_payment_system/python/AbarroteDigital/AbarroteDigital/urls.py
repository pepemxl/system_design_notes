"""AbarroteDigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from store.views import ProductListView, AddToCartView, CartView, CheckoutView
from store.views import PaymentProcessView
from store.views import PaymentConfirmationView
#from store.views import PaymentSuccessView
#from store.views import PaymentErrorView
#from store.views import PaymentCancelView
#from store.views import PaymentView




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('wallet/', include('cryptocurrency_wallet_app.urls')),
    path('', ProductListView.as_view(), name='product_list'),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/process/', PaymentProcessView.as_view(), name='payment_process'),
    path('payment/confirmation/', PaymentConfirmationView.as_view(), name='payment_confirmation'),
]

