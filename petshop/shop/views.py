from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from shop.admin import ClassificationAdmin
from .models import Animal, Classification
from .forms import AnimalForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import CreateView,View
from typing import Any, Dict
from .bot import send_registration_notification

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
    classification = get_object_or_404(Classification, pk=classification_id)
    animals = Animal.objects.filter(classification=classification)
    classifications = Classification.objects.all()
    context = {
        'animals': animals,
        'title': 'Категории',
        'classifications': classifications,
    }
    return render(request, 'shop/classification.html', context)


def view_animal(request, animal_id):
    animal_item = get_object_or_404(Animal, pk=animal_id)
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


class RegisterView(CreateView):
    """
    I Have Doc-String
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'shop/register.html'

    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        send_registration_notification.delay()
        return super().render_to_response(context, **response_kwargs)

class LoginView(View):
    form_class = UserLoginForm
    template_name = 'shop/login.html'

    def post(self, request):
        # logger.info(request)
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request):
        # logger.info(request)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        # logger.info(request)
        logout(request)
        return redirect('login')