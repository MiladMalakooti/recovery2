from django.shortcuts import render
from .models import Record

# Add the Cat class & list and view function below the imports
# class Record:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, input1, input2, input3, timestamp):
#         self.input1 = input1
#         self.input2 = input2
#         self.input3 = input3
#         self.timestamp = timestamp

# records = [
#     Record('Lolo', 'tabby', 'foul little demon', 3),
#     Record('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Record('Raven', 'black tripod', '3 legged cat', 4)
# ]

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def trackers_index(request):
    trackers = Tracker.objects.all()
    return render(request, 'trackers/index.html', { 'trackers': records })

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')