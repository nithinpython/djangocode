from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

# Create your views here.



def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        el = request.POST['email']
        np = request.POST['password']
        cp = request.POST['Cpassword']
        if np == cp:
            if User.objects.filter(username=un).exists():
                messages.info(request, "!! Username already exists !!")
                return redirect('register')
            elif User.objects.filter(email=el).exists():
                messages.info(request, "!! Email already exists !!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=un, first_name=fn, last_name=ln, email=el, password=np)
                user.save()
                print("User Created")
                return redirect('login')

        else:
            messages.info(request, "!! Password mismatch !!")
            return redirect('register')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        np = request.POST['password']
        user = auth.authenticate(username=un, password=np)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid details")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')