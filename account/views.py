from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import Account
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return render(request, 'index.html')
        
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username alreay exists!, please try with different username')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email already exists please try with a different username!")
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Password does not math!')
            return redirect('register')

        create_account = User.objects.create_user(username=username,email=email,password=password)
        create_account.save()
        messages.success(request, 'The message has been successfully created!')
        return redirect(request, 'login')
    
    return render(request, 'register.html')


def singnout(request):
    logout(request)
    return redirect('login')