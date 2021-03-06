# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main.views import initdb, getFolowersPursuers

urlpatterns = patterns('',
    url(r'^initdb/$', initdb),
    url(r'^folowers/$', getFolowersPursuers),
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include(admin.site.urls)),
)
