from django.urls import path
from content import views

urlpatterns = [
    path('flux', views.flux),
    path('critique', views.critique),
    path('follow', views.follow),
    path('modify_critique', views.modify_critique),
    path('modify_ticket', views.modify_ticket),
    path('posts', views.posts),
    path('ticket', views.ticket),
]