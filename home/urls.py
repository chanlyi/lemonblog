from data_analysis.views import *
from django.conf.urls import patterns, url, include
from home.views import *

urlpatterns = patterns('home.views',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^index/', IndexView, name='index'),
                       )
