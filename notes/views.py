from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    # object to be passed into template
    context_object_name = 'notes'

# handles exception already for non-existing notes
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

