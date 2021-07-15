from django.http.response import Http404, HttpResponse
from django.shortcuts import render

from .models import (
    Event,
    Look_and_feel,
    Registration
)

from .Forms import Event_Registration

def index(request):
    look = Look_and_feel.objects.get(active_status = 'c')
    events = Event.objects.filter(event_status = 'upcomming') #GET EVENT OBJECT  
    print(look)
   
    return render(request,"event_management/index.html",{'events': events,'look': look})  #SEND OBJECT

def events(request,event_id):
    # Get model
    if event_id:
        event = Event.objects.get(id = event_id)
        
        if events:
            form = Event_Registration()
            return render(request,"event_management/Register.html",{'event':event,'form':form})

    #query model
    #send result
    return Http404

def registration(request,event_id):
    # Get model
    if event_id:
        event = Event.objects.get(id = event_id)
        return render(request,"event_management/Register.html",{'event':event,'registration':True})

    #query model
    #send result
    return Http404

