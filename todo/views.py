from django.shortcuts import render

from .models import Entry

def index(request):
  print(request)
  return render(request, 'todo/index.html')


def entry(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  context = { 'entry': entry }
  print(context)
  return render(request, 'todo/entry.html', context)
