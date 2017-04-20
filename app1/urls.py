from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /app1/
    url(r'^$', views.index, name='index'),
    # ex: /app1/5/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /app1/5/results/
    url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /app1/5/vote/
    url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),
]
