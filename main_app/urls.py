from django.contrib import admin
# Add the include function to the import
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trackers/', views.trackers_index, name='index'),
    path('trackers/<int:tracker_id>/', views.trackers_detail, name='detail'),
]