from django.urls import path
from members import views

urlpatterns = [
    path('', views.index),
    path('inscription', views.inscription),

]