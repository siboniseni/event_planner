"""Models for the events application.

This module defines the database models for handling events and comments in a Django project.
"""

from django.db import models
from django.conf import settings


class Event(models.Model):
    """
    Represents an event with details such as title, description, date, time,
    location, and an optional image. Events can also include highlights
    and ticket pricing information.

    Attributes:
        title (CharField): The title of the event, limited to 200 characters.
        description (TextField): A detailed description of the event.
        date (DateField): The date on which the event will occur.
        time (TimeField): The time at which the event is scheduled.
        location (CharField): The location where the event takes place.
        image (ImageField): An optional image for the event, stored under 'uploads/events/'.
        highlights (TextField): A comma-separated list of event highlights.
        ticket_price (DecimalField): Optional field for event ticket pricing.
        organizer (ForeignKey): A reference to the user who organizes the event.
            Uses Django's AUTH_USER_MODEL.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/events/')
    highlights = models.TextField(blank=True, help_text="Comma-separated highlights of the event.")
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns:
            str: The title of the event.
        """
        return self.title


class Comment(models.Model):
    """
    Represents a comment on a specific event.

    Attributes:
        event (ForeignKey): The event this comment is associated with.
        name (CharField): The name of the commenter.
        text (TextField): The content of the comment.
        created_at (DateTimeField): The datetime when the comment was created.
    """

    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns:
            str: A short description displaying commenter name and event title.
        """
        return f"Comment by {self.name} on {self.event.title}"

