from django.conf.urls import url

from . import views
from app1.views import *

from django.views import generic

urlpatterns = [
    # ex: /app1/
    url(r'^$', views.index, name='index'),
    # ex: /app1/5/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /app1/5/results/
    url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /app1/5/vote/
    url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^req$', req),
    url(r'^data$', data),
    url(r'^extra$', generic.TemplateView.as_view(template_name='extra.html')),
    url(r'^list$', return_list),
    
]
