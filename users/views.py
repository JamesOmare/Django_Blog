from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def sign_up(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # confirm_password = request.POST['confirm_password']

        # if password == confirm_password:
        #     new_user = User.objects.create_user(
        #         username = username,
        #         email = email
        #     )

        #     new_user.set_password(password)
        #     new_user.save()
            
        #     return redirect('posts_home')
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, 'User created successfully')
                return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context) 

def login_user(request):
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password=password)

        if user:
            #stores user in session
            login(request, user)
            return redirect('posts_home')

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context) 

def logout_user(request):
    logout(request)
    return redirect('posts_home')
   