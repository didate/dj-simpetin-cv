

from django.urls import path
from resume import views


urlpatterns = [
    path('', views.home_view, name='home'),
]