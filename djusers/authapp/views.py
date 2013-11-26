from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.models import User
from authapp.forms import UserForm, SignupForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def signup_view(request):

    print "up top"
    if request.method == "POST":
        print "in here"
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    form.cleaned_data["username"],
                    form.cleaned_data["email"],
                    form.cleaned_data["password"],
                    )
            return HttpResponseRedirect("/account/loggedin/")
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/account/loggedin/")
        else:
            # Show an error page
            data =  {
                    "UserForm" : UserForm(),
                    "SignupForm" : SignupForm()
                    }
            return render(request, "authapp/auth.tmpl", data)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
  
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponse("Thanks for signing in")
        else:
            return HttpResponse("User name and password don't match")
    else:
        form = LoginForm()
        return render(request, 'login.tmpl',{"LoginForm":form})

