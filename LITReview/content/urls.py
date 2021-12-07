from django.urls import path
from content import views

app_name = 'content'
urlpatterns = [
    path('', views.flux, name='flux'),
    path('review/', views.review, name='review'),
    path('follow/', views.follow, name='follow'),
    path('modify_review/', views.modify_review, name='modify_review'),
    path('modify_ticket/', views.modify_ticket, name='modify_ticket'),
    path('posts/', views.posts, name='posts'),
    path('ticket/', views.ticket, name='ticket'),
    #path('ticket/<int:id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:id>/review/', views.ticket_review, name='ticket_review'),
    path('user_autocomplete/', views.user_autocomplete, name='user_autocomplete'),
]