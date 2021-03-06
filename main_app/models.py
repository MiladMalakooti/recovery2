from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# vvvv comment out below when trying to get local time
# from datetime import datetime
# import pytz

# tz_LA = pytz.timezone('America/Los_Angeles')
# datetime_LA = datetime.now(tz_LA)
# print("LA time:", datetime_LA.strftime("%H:%M"))

# ----------------------------

class Tracker(models.Model):
    tracker_name = models.CharField(max_length=100)
    label1 = models.CharField(max_length=100)
    label2 = models.CharField(max_length=100)
    label3 = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tracker_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tracker_id': self.id})

class Record(models.Model):
    input1 = models.IntegerField()
    input2 = models.IntegerField()
    input3 = models.IntegerField()
    timestamp = models.TimeField(auto_now_add=True)
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)

    def __int__(self):
        return self.input1, self.input2, self.input3

    class Meta:
        ordering = ['-timestamp']