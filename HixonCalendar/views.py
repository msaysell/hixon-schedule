from calendar import day_name
from django.views.generic.base import TemplateView
from django.db.models.functions import TruncDay
from schedule.models import Event
from collections import defaultdict
import operator

class RegularEventsView(TemplateView):

    template_name = "regular_events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        events = Event.objects.filter(rule__isnull=False).distinct('title')
        grouped_events = defaultdict(list)
        [grouped_events[e.start.weekday()].append(e) for e in events]
        context['events'] = [(day_name[k], sorted(v, key=lambda e: e.start.hour)) for k, v in sorted(grouped_events.items(), key=operator.itemgetter(0))]
        return context