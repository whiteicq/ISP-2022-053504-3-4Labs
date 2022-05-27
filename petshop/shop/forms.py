from django import forms
from .models import Classification


class AnimalForm(forms.Form):
    title = forms.CharField(max_length=30, label="Название:", widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=10000, required=False, label="Описание", widget=forms.Textarea(attrs={
    "class": "form-control",
    "rows": 7,
     }))
    price = forms.FloatField(min_value=1, label="Цена:", widget=forms.TextInput(attrs={"class": "form-control"}))
    weight = forms.FloatField(min_value=0.1, label="Вес:", widget=forms.TextInput(attrs={"class": "form-control"}))
    photo = forms.ImageField(required=False, label="Фото:")
    classification = forms.ModelChoiceField(queryset=Classification.objects.all(), empty_label="Выберите класс", label="Класс", widget=forms.Select(attrs={"class": "form-control"}))