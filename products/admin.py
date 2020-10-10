from django.contrib import admin
from .models import (
    Category,
    Dimension,
    ColorTubes,
    ColorElbow,
    Coating,
    ImageProduct,
    Products,
)

# register your models here.

admin.site.register(Category)
admin.site.register(Dimension)
admin.site.register(ColorTubes)
admin.site.register(ColorElbow)
admin.site.register(Coating)
admin.site.register(ImageProduct)
admin.site.register(Products)
