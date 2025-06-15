from django.urls import path

from . import views

urlpatterns = [
    path("", views.shop, name='shop'),
path("shop/", views.shop, name='shop'),
]