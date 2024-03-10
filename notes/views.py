from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

from .models import Notes

class NotesCreateView(CreateView):
    # what the endpoint is regarding
    model = Notes
    # attributes of the model
    fields = ['title', 'text']
    # redirect the user to the list of created/existing notes
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    # object to be passed into template
    context_object_name = 'notes'

# handles exception already for non-existing notes
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

