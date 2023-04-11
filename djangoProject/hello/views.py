from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
# context is a variable that stores information that we would like to provide to the template
    context = {}
    return render(request, 'hello.html', context)

def services(request):
# context is a variable that stores information that we would like to provide to the template
    context = {}
    return render(request, 'services.html', context)

def faq(request):
# context is a variable that stores information that we would like to provide to the template
    context = {}
    return render(request, 'faq.html', context)

def register(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
     # We use Django's UserCreationForm which is a model created by Django to create a new user.
     # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        form = UserCreationForm(request.POST)
    # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
        # redirect the user to login page so that after registration the user can enter the credentials
            return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
        # get the user info from the form data and log in the user
            user = form.get_user()
            login(request, user)
            return redirect('hello')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('hello')

@login_required(login_url='login_page')
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('hello')
    context = {'form': form}
    return render(request, 'contact.html', context)

def appointments(request):
# context is a variable that stores information that we would like to provide to the template
    context = {}
    return render(request, 'hello.html', context)