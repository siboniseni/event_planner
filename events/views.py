from django.shortcuts import redirect, render, get_object_or_404
from .models import Event, Comment
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.utils.timezone import now


def home(request):
    """
    Home view: Displays the latest 3 upcoming events, sorted by date.
    
    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: Rendered homepage with the latest 3 events.
    """
    events = Event.objects.filter(date__gte=now().date()).order_by('date')[:3]
    return render(request, 'events/homepage.html', {'events': events})


def event_list(request):
    """
    Event list view: Displays all events sorted by date in ascending order.
    
    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: Rendered event list page with all events.
    """
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    """
    Event detail view: Displays details for a specific event.
    
    Args:
        request (HttpRequest): The request object.
        pk (int): Primary key of the event.
    
    Returns:
        HttpResponse: Rendered event detail page with the event details.
    """
    event = get_object_or_404(Event, pk=pk)  # Fetch the event by primary key

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        # Save the new comment
        Comment.objects.create(event=event, name=name, text=text)

        return redirect('events:event_detail', pk=event.pk)  # Redirect to show the new comment
    
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def post_event(request):
    """
    Post event view: Allows logged-in users to create a new event.
    
    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: Rendered event creation page with a form.
    """
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Set the logged-in user as the organizer
            event.save()
            return redirect("events:event_list")  # Redirect to the event list
    else:
        form = EventForm()
    return render(request, "events/post_event.html", {"form": form})


def past_events(request):
    """
    Past events view: Displays all past events, sorted by the most recent first.
    
    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: Rendered past events page with all past events.
    """
    events = Event.objects.filter(date__lt=now().date()).order_by('-date')  # Sort by most recent past date
    return render(request, 'events/past_events.html', {'events': events})
