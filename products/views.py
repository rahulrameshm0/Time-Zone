from django.shortcuts import render
from django.contrib import messages
# from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def product_details(request):
    return render(request, 'latest.html')