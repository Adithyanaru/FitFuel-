from django.urls import path
from WepApp import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('shop/',views.shop,name='shop'),
    path('filtered_product/<cat_name>/',views.filtered_product,name='filtered_product'),
    path('single_page/<product_id>/',views.single_page,name='single_page'),
    path('contact/',views.contact,name='contact'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('save_account/',views.save_account,name='save_account'),
    path('user_loging/',views.user_loging,name='user_loging'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('shoping_cart/',views.shoping_cart,name='shoping_cart'),
    path('save_cart/',views.save_cart,name='save_cart'),
]
