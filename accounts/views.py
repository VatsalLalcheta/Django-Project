from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        pass2 = request.POST['pass2']
        if not pass2 == user_password: 
            messages.info(request, 'password does not match')
            return redirect('register')
        if User.objects.filter(username = user_name).exists():
            messages.info(request, 'User Name is already taken')
            return redirect('register')
        elif User.objects.filter(email = user_email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username = user_name, password=user_password, email = user_email, first_name = first_name, last_name = last_name)
            user.save()        
            print("user created")
        return redirect('feed')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        username = request.POST['user_name']
        passwrod = request.POST['user_password']

        user = auth.authenticate(username = username, password = passwrod)

        if user is not None:
            auth.login(request, user)
            return redirect('feed')
        
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')