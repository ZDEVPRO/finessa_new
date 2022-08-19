from django.contrib import admin
from contact.models import Aloqa


class AloqaAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'product_id', 'phone', 'create_date']
    readonly_fields = ['first_name', 'last_name', 'product_id', 'phone', 'ip', 'message', 'create_date']


admin.site.register(Aloqa, AloqaAdmin)
