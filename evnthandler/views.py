from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Attendee, Task

# Event Views
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        location = request.POST['location']
        date = request.POST['date']
        Event.objects.create(name=name, description=description, location=location, date=date)
        return redirect('event_list')
    return render(request, 'event_form.html')

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.name = request.POST['name']
        event.description = request.POST['description']
        event.location = request.POST['location']
        event.date = request.POST['date']
        event.save()
        return redirect('event_list')
    return render(request, 'event_form.html', {'event': event})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_confirm_delete.html', {'event': event})

# Attendee Views
def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'attendee_list.html', {'attendees': attendees})

def attendee_detail(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    return render(request, 'attendee_detail.html', {'attendee': attendee})

def attendee_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Attendee.objects.create(name=name, email=email)
        return redirect('event_list')
    return render(request, 'attendee_form.html')

def attendee_update(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    if request.method == 'POST':
        attendee.name = request.POST['name']
        attendee.email = request.POST['email']
        attendee.save()
        return redirect('attendee_list')
    return render(request, 'attendee_form.html', {'attendee': attendee})

def attendee_delete(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    if request.method == 'POST':
        attendee.delete()
        return redirect('attendee_list')
    return render(request, 'attendee_confirm_delete.html', {'attendee': attendee})

# Task Views
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        deadline = request.POST['deadline']
        status = request.POST['status']
        event_id = request.POST['event']
        attendee_id = request.POST.get('attendee')
        event = get_object_or_404(Event, pk=event_id)
        attendee = get_object_or_404(Attendee, pk=attendee_id) if attendee_id else None
        Task.objects.create(name=name, deadline=deadline, status=status, event=event, attendee=attendee)
        return redirect('task_list')
    events = Event.objects.all()
    attendees = Attendee.objects.all()
    return render(request, 'task_form.html', {'events': events, 'attendees': attendees})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.name = request.POST['name']
        task.deadline = request.POST['deadline']
        task.status = request.POST['status']
        event_id = request.POST['event']
        attendee_id = request.POST.get('attendee')
        task.event = get_object_or_404(Event, pk=event_id)
        task.attendee = get_object_or_404(Attendee, pk=attendee_id) if attendee_id else None
        task.save()
        return redirect('task_list')
    events = Event.objects.all()
    attendees = Attendee.objects.all()
    return render(request, 'task_form.html', {'task': task, 'events': events, 'attendees': attendees})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})