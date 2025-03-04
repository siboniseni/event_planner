"""Models for the events application.

This module defines the database models for handling events and comments in a Django project.

:module: events.models
:author: Siboniseni Kasa
"""

from django.db import models
from django.conf import settings


class Event(models.Model):
    """
    Represents an event with details such as title, description, date, time,
    location, and an optional image. Events can also include highlights
    and ticket pricing information.

    :ivar title: The title of the event.
    :ivar description: A detailed description of the event.
    :ivar date: The date on which the event will occur.
    :ivar time: The time at which the event is scheduled.
    :ivar location: The location where the event takes place.
    :ivar image: An optional image for the event, stored under 'uploads/events/'.
    :ivar highlights: A comma-separated list of event highlights.
    :ivar ticket_price: Optional field for event ticket pricing.
    :ivar organizer: A reference to the user who organizes the event.
    :type title: str
    :type description: str
    :type date: date
    :type time: time
    :type location: str
    :type image: str
    :type highlights: str
    :type ticket_price: decimal
    :type organizer: ForeignKey
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

    :ivar event: The event this comment is associated with.
    :ivar name: The name of the commenter.
    :ivar text: The content of the comment.
    :ivar created_at: The datetime when the comment was created.
    :type event: ForeignKey
    :type name: str
    :type text: str
    :type created_at: datetime
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

