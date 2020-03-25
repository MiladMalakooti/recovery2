from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tracker
from .forms import RecordForm

class TrackerCreate(CreateView):
    model = Tracker
    fields = '__all__'
    success_url = '/trackers/'

class TrackerUpdate(UpdateView):
  model = Tracker
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'

class TrackerDelete(DeleteView):
  model = Tracker
  success_url = '/trackers/'

def trackers_index(request):
    trackers = Tracker.objects.all()
    return render(request, 'trackers/index.html', { 'trackers': trackers })

def trackers_detail(request, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    record_form = RecordForm()
    return render(request, 'trackers/detail.html', {
         'tracker': tracker, 'record_form': record_form 
         })

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_record(request, tracker_id):
    form = RecordForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
        new_record = form.save(commit=False)
        new_record.tracker_id = tracker_id
        new_record.save()
    return redirect('detail', tracker_id=tracker_id)