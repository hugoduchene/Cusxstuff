# Generated by Django 3.1.2 on 2020-10-10 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fr', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_coating_fr', models.CharField(max_length=255)),
                ('name_coating_en', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ColorElbow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_color_fr', models.CharField(max_length=255)),
                ('name_color_en', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ColorTubes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_color_fr', models.CharField(max_length=255)),
                ('name_color_en', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('high', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_product', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product_fr', models.CharField(max_length=255)),
                ('name_product_en', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('Coating', models.ManyToManyField(blank=True, to='products.Coating')),
                ('color_elbow', models.ManyToManyField(to='products.ColorElbow')),
                ('color_tubes', models.ManyToManyField(to='products.ColorTubes')),
                ('dimension', models.ManyToManyField(to='products.Dimension')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('images_product', models.ManyToManyField(to='products.ImageProduct')),
            ],
        ),
    ]
