from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
  path('', views.index, name='index'),
  path('entry/<int:entry_id>/', views.entry, name='entry'),
  path('add/', views.new_entry, name='new_entry'),
]
