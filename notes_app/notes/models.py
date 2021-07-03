from django.db import models
from datetime import datetime

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title # Use the title as the field

