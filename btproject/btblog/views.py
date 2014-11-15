from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render
from django.template import RequestContext

from btblog.models import Entry


class EntryList(ListView):
    model = Entry
    template_name = "btblog/entry_list.html"
    paginate_by = 10
    
    # Can we sort with querysets instead?
    # then we could override get_queryset and avoid hijacking def get
    '''
    def get(self, request, *args, **kwargs):
        entries = list(Entry.objects.all())
        manual_entries = []
        for i in xrange(len(entries) - 1, -1, -1 ):
            if entries[i].order_manual:
                manual_entries.append(entries.pop(i))
                
        manual_entries.sort(key=lambda x: x.order_manual)
        for entry in manual_entries:
            entries.insert(int(entry.order_manual), entry)
        
        context = RequestContext(request, {'object_list': entries})

        return render(request, self.template_name, context)
    '''


class EntryDetail(DetailView):
    model = Entry
    template_name = "btblog/entry_detail.html"


class AboutPage(View):
    template_name = "btblog/about.html"
    model = None


class MusicPage(View):
    template_name = "btblog/music.html"
    model = Entry