from django.shortcuts import redirect, render, get_object_or_404
from .models import Event, Comment
from django.contrib.auth.decorators import login_required
from .forms import EventForm


# Home view: Display the latest 3 events, sorted by date
def home(request):
    events = Event.objects.all().order_by('date')[:3]  # Sort by date first, then limit to 3
    return render(request, 'events/homepage.html', {'events': events})


# Event list view: Display all events sorted by date in ascending order
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})


# Event detail view: Display details for a specific event
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Fetch the event by primary key

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        # Save the new comment
        Comment.objects.create(event=event, name=name, text=text)

        return redirect('events:event_detail', pk=event.pk)  # Redirect to the same event page to show the new comment
    
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def post_event(request):
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
