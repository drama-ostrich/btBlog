from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from django.utils import simplejson

from btblog.models import Entry

class EntryList(ListView):
    model = Entry
    template_name = "btblog/entry_list.html"
    
    # Can we sort with querysets instead?
    # then we could override get_queryset and avoid hijacking def get
    def get(self, request, *args, **kwargs):
        entries = list(Entry.objects.all())
        manual_entries = []
        for i in xrange(len(entries) - 1, -1, -1 ):
            if entries[i].order_manual:
                manual_entries.append(entries.pop(i))
                
        manual_entries.sort(key=lambda x: x.order_manual)
        for entry in manual_entries:
            entries.insert(int(entry.order_manual), entry)
        
        context = RequestContext (request, {'object_list' : entries})
        return render(request, self.template_name, context)
    
class EntryDetail(DetailView):
    model = Entry
    template_name = "btblog/entry_detail.html"
    
class AboutPage(View):
    template_name = "btblog/about.html"
    model = None
class MusicPage(View):
    template_name = "btblog/music.html"
    model = Entry