from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)  # Event title
    description = models.TextField()  # Detailed description
    date = models.DateField()  # Event date
    time = models.TimeField()  # Event time
    location = models.CharField(max_length=255)  # Event location
    image = models.ImageField(upload_to='uploads/events/')  # Event image
    highlights = models.TextField(blank=True, help_text="Comma-separated highlights of the event.")  # Key highlights

    def __str__(self):
        return self.title  # Return the event title as a string
