from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Record
from .models import Tracker

class TrackerCreate(CreateView):
    model = Tracker
    fields = ['tracker_name', 'label1', 'label2', 'label3']

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def trackers_index(request):
    trackers = Tracker.objects.all()
    return render(request, 'trackers/index.html', { 'trackers': trackers })

def trackers_detail(request, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    return render(request, 'trackers/detail.html', { 'tracker': tracker })

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')