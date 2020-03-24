from django.shortcuts import render
from .models import Record
from .models import Tracker

def trackers_detail(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def trackers_index(request):
    trackers = Tracker.objects.all()
    return render(request, 'trackers/index.html', { 'trackers': trackers })

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')