from django.contrib import admin
from .models import Animal, Classification


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'classification', 'title', 'price', 'weight', 'created_at', 'is_sales')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    list_editable = ('is_sales',)
    list_filter = ('is_sales', 'classification')

class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Classification, ClassificationAdmin)