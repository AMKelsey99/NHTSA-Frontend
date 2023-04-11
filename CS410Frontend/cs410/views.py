from django.shortcuts import render, redirect
# from .forms import placeholderform
from .models import placeholder
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import UpdateView
from simple_history.models import HistoricalRecords

# AUTH FUNCTIONS #

# Function to check if the user is an Admin
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

# Function to check if the user is an Underwriter
def is_underwriter(user):
    return user.groups.filter(name='Underwriter').exists()

# Default group upon registration unless the Admin adds the user to Underwriter or Admin
# Function to check if the user is an Admin
def is_Guest(user):
    return user.groups.filter(name='Guest').exists()

class UserProfileUpdateView(UpdateView):
    model = User
    
    def get_initial(self):
        initial = super(UserProfileUpdateView, self).get_initial()
        return initial
    
    def get_form_class(self):
        return UserProfileForm
    
    def form_valid(self, form):
        return super(UserProfileUpdateView, self).form_valid(form)

# PAGE VIEWS #

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
            user =  form.save()
            group = Group.objects.get(name='Guest')
            user.groups.add(group)
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

@login_required(login_url='accounts/login/')
@user_passes_test(is_admin)
def history(request):
    context = {'history_table': placeholder.history.all()}
    return render(request, 'history.html', context)

@login_required(login_url='accounts/login/')
@user_passes_test(is_admin)
def adminview(request):
    return redirect('admin:index')

def afield1(request):
    entry = placeholder.objects.all().order_by('field1').values()
    context = {'placeholder_table': entry}
    return render(request,'main.html',context)

def afield2(request):
    entry = placeholder.objects.all().order_by('field2').values()
    context = {'placeholder_table': entry}
    return render(request,'main.html',context)

def afield3(request):
    entry = placeholder.objects.all().order_by('field3').values()
    context = {'placeholder_table': entry}
    return render(request,'main.html',context)

def dfield1(request):
    entry = placeholder.objects.all().order_by('-field1').values()
    context = {'placeholder_table': entry}
    return render(request,'main.html',context)

def dfield2(request):
    entry = placeholder.objects.all().order_by('-field2').values()
    context = {'placeholder_table': entry}
    return render(request,'main.html',context)

def dfield3(request):
    entry = placeholder.objects.all().order_by('-field3').values()
    context = {'placeholder_table': entry}
    return render(request,'main.html',context)

def delete(request, id):
    entry = placeholder.objects.get(id=id)
    entry.delete()
    return redirect('main')
