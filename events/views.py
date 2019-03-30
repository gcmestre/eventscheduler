from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .models import Event
from django.http import Http404


class EventList(generic.ListView):
    model = Event
    paginate_by = 25
    ordering = ['date']

    def get_queryset(self):
        """Return the next events order by date"""
        return Event.objects.filter(date__gte=timezone.now()).order_by('date')


class EventCreate(generic.CreateView):
    model = Event
    fields = ['title', 'description', 'date']
    success_url = "/"


    def form_valid(self, form):
        """
        Sets the owner of the created event as the logged in User
        """
        event = form.save(commit=False)
        event.owner = self.request.user
        return super(EventCreate, self).form_valid(form)


class EventDetail(generic.DetailView):
    model = Event


class EventUpdate(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'date']

    success_url = "/"

    def post(self, request, *args, **kwargs):
        """
        Validates that the user making the request is the owner of the event otherwise will raise an 404
        """
        self.object = self.get_object()
        if request.user and request.user == self.object.owner:
            return super().post(request, *args, **kwargs)
        else:
            raise Http404

    def form_valid(self, form):
        """
        Sets the owner of the created event as the logged in User
        """
        event = form.save(commit=False)
        event.owner = self.request.user
        return super(EventUpdate, self).form_valid(form)


class EventSubscribe(generic.View):

    def get(self, request, *args, **kwargs):
        """
            Adds the logged in User to the event subscribed list.
            Increments the number of user subscribed to the event by one
        """
        # get Event
        event = get_object_or_404(Event, pk=kwargs['pk'])
        # Add User to the event subscribed list
        event.number_of_subscribers = event.number_of_subscribers + 1
        event.subscribers.add(request.user)
        event.save()
        return redirect('events:list')


class EventUnsubscribe(generic.View):

    def get(self, request, *args, **kwargs):
        """
            Removes the logged in User from the event subscribed list.
            Reduces the number of users subscribed to the event by one
        """
        # get Event
        event = get_object_or_404(Event, pk=kwargs['pk'])
        event.number_of_subscribers = event.number_of_subscribers - 1
        # Add User to the event subscribed list
        event.subscribers.remove(request.user)
        event.save()
        return redirect('events:list')
