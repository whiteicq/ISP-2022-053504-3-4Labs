from statistics import mode
from tabnanny import verbose
from django.db import models
from django.urls import reverse

class Animal(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(max_length=10000, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    weight = models.FloatField(verbose_name='Вес')
    photo = models.ImageField(blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_sales = models.BooleanField(default=False, verbose_name='Продано?')
    classification = models.ForeignKey('Classification', on_delete=models.PROTECT, null=True, verbose_name='Класс')

    def get_absolute_url(self):
        return reverse('view_animal', kwargs={"animal_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
        ordering = ['-created_at']


class Classification(models.Model): 
    title = models.CharField(max_length=40, db_index=True, verbose_name="Класс")

    def get_absolute_url(self):
        return reverse('classification', kwargs={"classification_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = 'Классы'
        ordering = ['title'] 
    

