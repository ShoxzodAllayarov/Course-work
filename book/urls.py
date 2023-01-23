from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.index, login_url='/login'), name='index'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    re_path(r'add/$', views.book_add, name='book_add'),

    re_path(r'cart/add/(?P<slug>[\w-]+)/$', views.cart_add, name='cart_add'),
    re_path(r'cart/delete/(?P<slug>[\w-]+)/$', views.cart_delete, name='cart_delete'),
    re_path(r'cart/list/$', views.cart_list, name='cart_list'),
]