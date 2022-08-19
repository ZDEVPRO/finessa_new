from django.shortcuts import render, redirect
from shop.models import Product, Images
from django.core.paginator import Paginator
from home.forms import AloqaForm
from contact.models import Aloqa
from django.contrib import messages


def index(request):
    return render(request, 'index/base.html')


def shop(request):
    product_home = Product.objects.all().order_by('-id')
    product_paginator = Paginator(product_home, per_page=12)
    page_number = request.GET.get('page', 1)
    page_obj = product_paginator.get_page(page_number)
    context = {
        'product_home': page_obj.object_list,
        'product_paginator': product_paginator,
        'page_number': int(page_number),
    }
    return render(request, 'shop/base.html', context)


def shop_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {
        'product': product,
        'images': images
    }
    return render(request, 'shop_detail/base.html', context)


def about(request):
    return render(request, 'about/base.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def contact(request, id, slug):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            data = Aloqa()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.product_id = form.cleaned_data['product_id']
            data.message = form.cleaned_data['message']
            data.ip = get_client_ip(request)
            data.save()
            messages.success(request, 'Buyurtmangiz qabul qilindi, tez orada siz bilan bog`lanamiz. Raxmat!')
            return redirect('contact', id, slug)
    form = AloqaForm

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'contact/base.html', context)
