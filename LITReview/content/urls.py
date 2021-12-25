from django.urls import path
from content import views

app_name = "content"
urlpatterns = [
    path("", views.flux, name="flux"),
    path("review/", views.review, name="review"),
    path("review/<int:review_id>/", views.review_update, name="review_update"),
    path("review/<int:review_id>/delete/", views.review_delete, name="review_delete"),
    path("follow/", views.follow, name="follow"),
    path("unfollow/<int:follow_id>/", views.unfollow, name="unfollow"),
    path("posts/", views.posts, name="posts"),
    path("ticket/", views.ticket, name="ticket"),
    path("ticket/<int:ticket_id>/", views.ticket_detail, name="ticket_detail"),
    path("ticket/<int:ticket_id>/update/", views.ticket_update, name="ticket_update"),
    path("ticket/<int:ticket_id>/delete/", views.ticket_delete, name="ticket_delete"),
]
