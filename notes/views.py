from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm
from .models import Notes

class NotesCreateView(CreateView):
    # what the endpoint is regarding
    model = Notes
    # redirect the user to the list of created/existing notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    # object to be passed into template
    context_object_name = 'notes'

# handles exception already for non-existing notes
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

class NotesUpdateView(UpdateView):
    model = Notes
    # redirect the user to the list of created/existing notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
