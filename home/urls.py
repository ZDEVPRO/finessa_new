from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/<int:id>/<slug:slug>', views.contact, name='contact'),
    path('shop/<int:id>/<slug:slug>', views.shop_detail, name='shop_detail'),
]
