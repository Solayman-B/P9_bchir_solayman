from django.urls import path
from members import views

urlpatterns = [
    path('', views.login),
    path('register', views.register),
]