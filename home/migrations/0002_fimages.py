# Generated by Django 3.2.13 on 2022-04-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='Fimages/')),
                ('image2', models.ImageField(upload_to='Fimages/')),
                ('image3', models.ImageField(upload_to='Fimages/')),
                ('image4', models.ImageField(upload_to='Fimages/')),
            ],
            options={
                'verbose_name': 'F Images',
                'verbose_name_plural': 'F Images',
            },
        ),
    ]
