from django.db import models
from django.conf import settings


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    date = models.DateField()  
    time = models.TimeField()  
    location = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='uploads/events/')  
    highlights = models.TextField(blank=True, help_text="Comma-separated highlights of the event.")  
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Ticket price (optional)
    
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,  # Allow null for existing rows
        blank=True  # Allow blank values in forms
    )
    
    def __str__(self):
        return self.title  # Return the event title as a string


class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)  # Link to the event
    name = models.CharField(max_length=100) 
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Comment by {self.name} on {self.event.title}"
    
