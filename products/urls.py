from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('latest', views.product_details, name='latest')
]
    