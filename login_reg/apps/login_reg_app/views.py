from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    if 'username' in request.session:
        return render(request, 'login_reg_app/loggedin.html')
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
        else:
            messages.info(request, "Successfully Registered")
            User.objects.add_user(request.POST)
        return redirect('/')
    return render(request, 'login_reg_app/index.html')


def login(request):
    if User.objects.login_valid(request.POST):
            request.session['username'] = request.POST['username']
    else:
        messages.info(request, "Login Unsuccessful")
    return redirect('/')


def logout(request):
    del request.session['username']
    return redirect('/')