# Generated by Django 3.2.13 on 2022-04-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_fimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='fimages',
            name='image1_link',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='fimages',
            name='image2_link',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='fimages',
            name='image3_link',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='fimages',
            name='image4_link',
            field=models.CharField(blank=True, max_length=800),
        ),
    ]
