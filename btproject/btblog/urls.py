# btblog/urls.py
from django.conf import settings

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from btblog import views

urlpatterns = patterns("",
    # /
    url(
        regex=r"^$",
        view=views.EntryList.as_view(),
        name='entry_list'
    ),

    # /entry/{id}
    url(
        regex=r'^entry/(?P<pk>\d+)/$',
        view=views.EntryDetail.as_view(),
        name='entry_detail'
    ),

    url(r'^about/', TemplateView.as_view(template_name="btblog/about.html"), name='page_about'),
    
    url(r'^music/', TemplateView.as_view(template_name="btblog/music.html"), name='page_music'),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))