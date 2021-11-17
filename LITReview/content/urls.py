from django.urls import path
from content import views

app_name = 'content'
urlpatterns = [
    path('', views.flux),
    path('review/', views.review),
    path('follow/', views.follow),
    path('modify_review/', views.modify_review),
    path('modify_ticket/', views.modify_ticket),
    path('posts/', views.posts),
    path('ticket/', views.ticket),
]