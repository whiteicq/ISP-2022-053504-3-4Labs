from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from shop.admin import ClassificationAdmin
from .models import Animal, Classification

# Create your views here.


def index(request):
    animals = Animal.objects.order_by('-created_at')
    classifications = Classification.objects.all()
    context = {
    'animals': animals,
    'title': 'Список животных',
    'classifications': classifications,
    }
    return render(request, 'shop/index.html', context)

def get_classification(request, classification_id):
    animals = Animal.objects.filter(classification = classification_id)
    classifications = Classification.objects.all()
    #classification = Classification.objects.get(pk=classification_id)
    context = {
    'animals': animals,
    'classifications': classifications,
    #'classification': classification,
    }
    return render(request, 'shop/classification.html', context)