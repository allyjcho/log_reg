from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('create_msg', views.create_msg),
    path('create_cmt/<int:msg_id>', views.add_cmt)
]
