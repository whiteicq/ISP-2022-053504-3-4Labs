import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from shop.admin import ClassificationAdmin
from .models import Animal, Classification
from .forms import AnimalForm

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