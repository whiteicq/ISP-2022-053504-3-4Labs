from django import forms
from .models import Classification
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Адрес почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AnimalForm(forms.Form):
    title = forms.CharField(max_length=30, label="Название:", widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=10000, required=False, label="Описание", widget=forms.Textarea(attrs={
    "class": "form-control",
    "rows": 7,
     }))
    seller_number = forms.CharField(max_length=13, label='Номер продавца', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(min_value=1, label="Цена:", widget=forms.TextInput(attrs={"class": "form-control"}))
    weight = forms.FloatField(min_value=0.1, label="Вес:", widget=forms.TextInput(attrs={"class": "form-control"}))
    photo = forms.ImageField(required=False, label="Фото:")
    classification = forms.ModelChoiceField(queryset=Classification.objects.all(), empty_label="Выберите класс", label="Класс", widget=forms.Select(attrs={"class": "form-control"}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не может начинаться с цифр')
        return title