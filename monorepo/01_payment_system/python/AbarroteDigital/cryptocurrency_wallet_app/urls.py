from django.urls import path
from . import views

urlpatterns = [
    path('wallet/', views.wallet, name='wallet'),
    path('send/', views.send, name='send'),
    path('receive/', views.receive, name='receive'),
]