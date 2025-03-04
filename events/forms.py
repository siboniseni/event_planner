"""Forms for the events application.

This module defines the form used to create and edit events in the Django project.

:module: events.forms
:author: Siboniseni
"""

from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    A form for creating and editing events.

    This form uses the `Event` model and includes fields such as title,
    description, date, time, location, image, and ticket price. It customizes
    the widgets for each field to apply specific CSS classes and HTML attributes.

    :class: EventForm
    """

    class Meta:
        model = Event
        fields = ["title", "description", "date", "time", "location", "image", "ticket_price"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ticket_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

