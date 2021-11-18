from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from .forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html', next_page='accounts:login'), name='logout'),
    path('register/', views.register, name='register')
]