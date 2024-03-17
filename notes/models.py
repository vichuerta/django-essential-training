from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    # Limited Text Field
    title = models.CharField(max_length=200)
    text = models.TextField()
    # Every time a note is created, this field will be automatically populated with the time it was created 
    created = models.DateTimeField(auto_now_add=True)
    # if a user gets deleted, we also want to delete all the notes associated with them
    # identify this relationship on the user side
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")