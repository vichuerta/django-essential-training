from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

class NotesCreateView(CreateView):
    # what the endpoint is regarding
    model = Notes
    # redirect the user to the list of created/existing notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    # object to be passed into template
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    # if a user tries to access the list view and it's not logged in, they will be redirected to this page instead of seeing a 404
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

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
