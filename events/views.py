from django.shortcuts import render, get_object_or_404
from .models import Event
from django.core.paginator import Paginator


# Home view: Display the latest 3 events
def home(request):
    events = Event.objects.all()[:3]  # Fetch the latest 3 events
    return render(request, 'events/homepage.html', {'events': events})


# Event list view: Display all events
def event_list(request):
    events = Event.objects.all()
    paginator = Paginator(events, 9)  # Show 9 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/event_list.html', {'events': events})


# Event detail view: Display details for a specific event
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Fetch the event by primary key
    return render(request, 'events/event_detail.html', {'event': event})
