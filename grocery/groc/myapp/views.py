from django.shortcuts import render, redirect
from .models import Grocery
from .forms import GroceryForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        #check if user has entered correct crendentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/welcome')
        else:
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def welcome(request):
    return render(request, "welcome.html")

def load_form(request): 
    form = GroceryForm
    return render(request, "index.html", {'form':form})

def add(request):
    form = GroceryForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    grocery = Grocery.objects.all
    return render(request, "show.html", {'grocery': grocery})

def edit(request, id):
    grocery = Grocery.objects.get(id=id)
    return render(request, "edit.html", {'grocery':grocery})

def update(request, id):
    grocery = Grocery.objects.get(id=id)
    form = GroceryForm(request.POST, instance=grocery)
    form.save()
    return redirect('/show')

def delete(request, id):
    grocery = Grocery.objects.get(id=id)
    grocery.delete()
    return redirect('/show')

def search(request):
    given_name = request.POST['name']
    grocery = Grocery.objects.filter(name__icontains = given_name).order_by('date')
    return render(request, "show.html", {'grocery':grocery})

def logoutuser(request):
    logout(request)
    return redirect('/login')