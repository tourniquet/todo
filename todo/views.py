from django.shortcuts import render

from .models import Entry

def index(request):
  entries = Entry.objects.order_by('date_added')
  context = { 'entries': entries }
  return render(request, 'todo/index.html', context)


def entry(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  context = { 'entry': entry }
  print(context)
  return render(request, 'todo/entry.html', context)
