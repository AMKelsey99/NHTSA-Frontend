from django.shortcuts import render, redirect
# from .forms import placeholderform
from .models import placeholder
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main(request):
    context = {'placeholder_table':placeholder.objects.all()}
    return render(request, 'main.html', context)

def search(request):
    model = placeholder;
    query = request.GET.get("searchterm") or ''
    entry = placeholder.objects.filter(field1__contains=query) or placeholder.objects.filter(field2__contains=query) or placeholder.objects.filter(field3__contains=query)
    context = {'placeholder_table': entry}
    return render(request, 'main.html', context)

def entryview(request, id):
    entry = placeholder.objects.get(id=id)
    context = {'entry':entry}
    return render(request, 'entry.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main')

