from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(password=password, username=username)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        psw = request.POST['psw']
        psw1 = request.POST['psw1']
        if psw1 == psw:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, password=psw, first_name=name, last_name=last_name,
                                                email=email)

                user.save()

        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('login')

    return render(request, 'register.html')
