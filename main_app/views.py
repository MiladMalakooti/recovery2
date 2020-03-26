from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tracker, Record
from .forms import RecordForm

class TrackerCreate(LoginRequiredMixin, CreateView):
    model = Tracker
    fields = ['tracker_name', 'label1', 'label2', 'label3']
    success_url = '/trackers/'

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class TrackerUpdate(LoginRequiredMixin, UpdateView):
  model = Tracker
  fields = '__all__'

class TrackerDelete(LoginRequiredMixin, DeleteView):
  model = Tracker
  success_url = '/trackers/'

@login_required
def trackers_index(request):
    trackers = Tracker.objects.filter(user=request.user)
    return render(request, 'trackers/index.html', { 'trackers': trackers })

@login_required
def trackers_detail(request, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    # record = Record.objects.get(id=record_id)
    record_form = RecordForm()
    arr = [tracker.label1, tracker.label2, tracker.label3]
    # caroline = [record.input1, record.input2, record.input3]
    form_list = zip(record_form, arr)
    # print(type(form_list))
    # print(caroline)
    return render(request, 'trackers/detail.html', {
         'tracker': tracker, 'record_form': record_form, 'arr': arr, 'form_list': form_list, #'caroline': caroline,
         })

@login_required
def home(request):
  return render(request, 'home.html')

@login_required
def about(request):
    return render(request, 'about.html')

rec_arr = []

@login_required
def add_record(request, tracker_id):
    form = RecordForm(request.POST)
    if form.is_valid():
        new_record = form.save(commit=False)
        new_record.tracker_id = tracker_id
        new_record.save()
        rec_arr.append(new_record.__dict__)
        print(new_record.__dict__)
        print(rec_arr)
    return redirect('detail', tracker_id=tracker_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
