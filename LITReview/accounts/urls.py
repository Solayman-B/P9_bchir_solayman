from django.urls import path
from django.contrib.auth import views
from accounts import views as mviews


urlpatterns = [
    path('', views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user = True)),
    path('logout/', views.LogoutView.as_view(template_name='accounts/logout.html')),
    path('register/', mviews.register)
]