from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from shop.admin import ClassificationAdmin
from .models import Animal, Classification
from .forms import AnimalForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.


def index(request):
    animals = Animal.objects.order_by('-created_at')
    classifications = Classification.objects.all()
    context = {
    'animals': animals,
    'title': 'Зоомагазин',
    'classifications': classifications,
    }
    return render(request, 'shop/index.html', context)

def get_classification(request, classification_id):
    animals = Animal.objects.filter(classification = classification_id)
    classifications = Classification.objects.all()
    #classification = Classification.objects.get(pk=classification_id)
    context = {
    'animals': animals,
    'title': 'Категории',
    'classifications': classifications,
    #'classification': classification,
    }
    return render(request, 'shop/classification.html', context)


def view_animal(request, animal_id):
    animal_item = Animal.objects.get(pk=animal_id)
    context = {
        'animal_item': animal_item
    }
    return render(request, 'shop/view_animal.html', context)


def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animals = Animal.objects.create(**form.cleaned_data)
            # return redirect('home')
            return redirect(animals)
    else:
        form = AnimalForm() 
    return render(request, 'shop/add_animal.html', {'form': form})


def register(request):
    if request == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('login')
        else:
            messages.error(request, 'Что-то пошло не так. Попробуйте заново')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {'form': form})


def user_login(request):
    if request == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = UserLoginForm()
    return render(request, 'shop/login.html', {'form': form})