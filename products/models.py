from django.db import models

# Create your models here.


class Category(models.Model):
    name_fr = models.CharField(max_length=255, blank=False, null=False)
    name_en = models.CharField(max_length=255, blank=False, null=False)


class Dimension(models.Model):
    length = models.IntegerField(blank=False, null=False)
    width = models.IntegerField(blank=False, null=False)
    high = models.IntegerField(blank=False, null=False)


class ColorTubes(models.Model):
    name_color_fr = models.CharField(max_length=255, null=False, blank=False)
    name_color_en = models.CharField(max_length=255, null=False, blank=False)


class ColorElbow(models.Model):
    name_color_fr = models.CharField(max_length=255, null=False, blank=False)
    name_color_en = models.CharField(max_length=255, null=False, blank=False)


class Coating(models.Model):
    name_coating_fr = models.CharField(max_length=255, null=False, blank=False)
    name_coating_en = models.CharField(max_length=255, null=False, blank=False)


class ImageProduct(models.Model):
    image_product = models.ImageField(upload_to='')


class Products(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_product_fr = models.CharField(max_length=255, blank=False, null=False)
    name_product_en = models.CharField(max_length=255, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    dimension = models.ManyToManyField(Dimension)
    color_tubes = models.ManyToManyField(ColorTubes)
    color_elbow = models.ManyToManyField(ColorElbow)
    Coating = models.ManyToManyField(Coating, blank=True)
    images_product = models.ManyToManyField(ImageProduct)
