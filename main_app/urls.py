from django.contrib import admin
# Add the include function to the import
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trackers/', views.trackers_index, name='index'),
    path('trackers/<int:tracker_id>/', views.trackers_detail, name='detail'),
    path('trackers/create/', views.TrackerCreate.as_view(), name='trackers_create'),
    path('trackers/<int:pk>/update/', views.TrackerUpdate.as_view(), name='trackers_update'),
    path('trackers/<int:pk>/delete/', views.TrackerDelete.as_view(), name='trackers_delete'),
    path('trackers/<int:tracker_id>/add_record/', views.add_record, name='add_record'),
    
]