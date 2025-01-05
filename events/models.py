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
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Ticket price (optional)

    def __str__(self):
        return self.title  # Return the event title as a string


class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)  # Link to the event
    name = models.CharField(max_length=100)  # Commenter's name
    text = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the comment

    def __str__(self):
        return f"Comment by {self.name} on {self.event.title}"
    