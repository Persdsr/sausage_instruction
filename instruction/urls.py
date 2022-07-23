from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<slug:instr>/', views.PostView.as_view(), name='post_detail'),
]
