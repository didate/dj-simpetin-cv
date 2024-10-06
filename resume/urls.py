

from django.urls import path
from resume import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'), 
    path('login/', auth_views.LoginView.as_view(template_name='resume/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('resume/<int:resume_id>/', views.resume_detail, name='resume_detail'),
]