import json, os
from calendar import day_name
from django.views.generic.base import TemplateView
from django.db.models.functions import TruncDay
from schedule.models import Event
from collections import defaultdict
from googleapiclient.discovery import build
from google.oauth2 import service_account
import operator
from django.http import JsonResponse


class CalendarView(TemplateView):
    template_name = "calendar_google.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key'] = "AIzaSyAycp2F-JgRuAJruRQYQyPnOIxsammdPok"
        context['calendar_id'] = "cipcc5ogpe5tlmt2lglout8qg4@group.calendar.google.com"
        return context


class RegularEventsView(TemplateView):

    template_name = "regular_events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        events = Event.objects.filter(rule__isnull=False).distinct('title')
        grouped_events = defaultdict(list)
        [grouped_events[e.start.weekday()].append(e) for e in events]
        context['events'] = [(day_name[k], sorted(v, key=lambda e: e.start.hour)) for k, v in sorted(grouped_events.items(), key=operator.itemgetter(0))]
        return context

def get_recurrent_events(request):
    calendar_id = "cipcc5ogpe5tlmt2lglout8qg4@group.calendar.google.com"
    info = json.loads(os.environ.get('GOOGLE_CALENDAR_CREDS'))
    creds = service_account.Credentials.from_service_account_info(info)
    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(calendarId=calendar_id, singleEvents=False).execute()
    g_events = [evt for evt in events_result.get('items', []) if evt.get('recurrence') is not None]
    return JsonResponse(g_events, safe=False)
