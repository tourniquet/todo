from django.shortcuts import render, redirect

from .models import Entry

def index(request):
  owner = request.user
  entries = Entry.objects.filter(owner=owner).order_by('-date_added')
  context = { 'entries': entries }
  return render(request, 'todo/index.html', context)


def entry(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  context = { 'entry': entry }
  print(context)
  return render(request, 'todo/entry.html', context)


def new_entry(request):
  title = request.POST['title']
  Entry.objects.create(text=title)

  return redirect('todo:index')
