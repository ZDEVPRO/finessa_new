from django.db import models


class Aloqa(models.Model):
    first_name = models.CharField('Ism', max_length=100)
    last_name = models.CharField('Familiya', max_length=100)
    phone = models.CharField('Telefon', max_length=50)
    product_id = models.CharField('Maxsulot Id raqami', max_length=50)
    message = models.TextField('Mijoz Manzili va xabari', max_length=1000)
    create_date = models.DateTimeField('Xabar kelgan vaqt', auto_now=True)
    ip = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Buyurtmalar'
        verbose_name_plural = 'Buyurtmalar'
