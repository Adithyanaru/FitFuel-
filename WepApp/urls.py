from django.urls import path
from WepApp import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('shop/',views.shop,name='shop'),
    path('filtered_product/<cat_name>/',views.filtered_product,name='filtered_product'),
]
