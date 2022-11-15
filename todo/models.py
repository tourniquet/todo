from django.db import models

class Entry(models.Model):
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'entries'

  def __str__(self):
    return f'{self.text[:50]}...'
