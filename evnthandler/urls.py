from django.urls import path
from evnthandler import views

urlpatterns = [
    # Event URLs
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/update/', views.event_update, name='event_update'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),

    # Attendee URLs
    path('attendees/', views.attendee_list, name='attendee_list'),
    path('attendees/create/', views.attendee_create, name='attendee_create'),
    path('attendees/<int:pk>/', views.attendee_detail, name='attendee_detail'),
    path('attendees/<int:pk>/update/', views.attendee_update, name='attendee_update'),
    path('attendees/<int:pk>/delete/', views.attendee_delete, name='attendee_delete'),

    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]