from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    title = models.TextField('Sarlavha', max_length=500)
    slug = models.CharField('Link', max_length=300)

    image = models.ImageField('Rasm', upload_to='product/')
    price = models.CharField('Narxi', max_length=300)

    delivery = models.TextField('Yetkazib berish', max_length=500)
    colors = models.TextField('Ranglar', max_length=500, blank=True)

    add_desc = models.TextField('Qisqa malumot', max_length=600, blank=True)
    sub_description = models.TextField('Malumot 1', max_length=1000)
    all_description = models.TextField('Malumot 2', max_length=3000, blank=True)
    add_info = RichTextUploadingField('Qo`shimcha malumot', blank=True)

    contact_number = models.TextField('Aloqa telefoni', max_length=700, blank=True)
    contact_address = models.TextField('Manzil', max_length=700, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField('Sarlavha', max_length=50, blank=True)
    image = models.ImageField('Rasm', blank=True, upload_to='images/')

    def __str__(self):
        return self.title
