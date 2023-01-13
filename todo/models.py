from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, timedelta

one_week = datetime.now() + timedelta(days=7)

class Entry(models.Model):
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  due_by = models.DateTimeField(default=one_week)
  is_completed = models.BooleanField(default=False)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'entries'

  def __str__(self):
    return f'{self.text}'
