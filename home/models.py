from ckeditor.fields import RichTextField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class HomeAboutSection(models.Model):
    content = RichTextField()

    class Meta:
        verbose_name = 'Home About Section'
        verbose_name_plural = 'Home About Section'


class HomeLogo(models.Model):
    logo = models.ImageField(upload_to='logo/')

    class Meta:
        verbose_name = 'Home Logo'
        verbose_name_plural = 'Home Logo'


class HomeTitle(models.Model):
    video = models.FileField('Background Video', upload_to='video/', blank=True)
    image = models.ImageField('Logo image', upload_to='image/logo/', blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=1000)

    button = models.TextField(max_length=300)
    button_link = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Home Title'
        verbose_name_plural = 'Home Title'

class FImages(models.Model):
    image1 = models.ImageField(upload_to='Fimages/')
    image1_link = models.CharField(max_length=800, blank=True)
    image2 = models.ImageField(upload_to='Fimages/')
    image2_link = models.CharField(max_length=800, blank=True)
    image3 = models.ImageField(upload_to='Fimages/')
    image3_link = models.CharField(max_length=800, blank=True)
    image4 = models.ImageField(upload_to='Fimages/')
    image4_link = models.CharField(max_length=800, blank=True)

    class Meta:
        verbose_name = 'F Images'
        verbose_name_plural = 'F Images'
