# Generated by Django 3.2.13 on 2022-04-18 08:25

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500, verbose_name='Sarlavha')),
                ('slug', models.CharField(max_length=300, verbose_name='Link')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Rasm')),
                ('price', models.CharField(max_length=300, verbose_name='Narxi')),
                ('delivery', models.TextField(max_length=500, verbose_name='Yetkazib berish')),
                ('colors', models.TextField(blank=True, max_length=500, verbose_name='Ranglar')),
                ('add_desc', models.TextField(blank=True, max_length=600, verbose_name='Qisqa malumot')),
                ('sub_description', models.TextField(max_length=1000, verbose_name='Malumot 1')),
                ('all_description', models.TextField(blank=True, max_length=3000, verbose_name='Malumot 2')),
                ('add_info', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Qo`shimcha malumot')),
                ('contact_number', models.TextField(blank=True, max_length=700, verbose_name='Aloqa telefoni')),
                ('contact_address', models.TextField(blank=True, max_length=700, verbose_name='Manzil')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Sarlavha')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Rasm')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
