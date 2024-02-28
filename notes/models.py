from django.db import models

# Create your models here.

class Notes(models.Model):
    # Limited Text Field
    title = models.CharField(max_length=200)
    text = models.TextField()
    # Every time a note is created, this field will be automatically populated with the time it was created 
    created = models.DateTimeField(auto_now_add=True)