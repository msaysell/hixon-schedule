from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, FormView
from schedule import urls as schedule_urls
from schedule.views import FullCalendarView
from HixonCalendar.views import RegularEventsView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('booking/', TemplateView.as_view(template_name='booking.html'), name='booking'),
    path('calendar/', FullCalendarView.as_view(template_name='calendar.html'), name='calendar', kwargs={'calendar_slug': 'hixon'}),
    path('committee/', TemplateView.as_view(template_name='committee.html'), name='committee'),
    path('100-club/', TemplateView.as_view(template_name='hundred_club.html'), name='hundred_club'),
    path('regular-events/', RegularEventsView.as_view(), name='regular_events'),
    path('schedule/', include(schedule_urls)),
    path('admin/', admin.site.urls)
]
