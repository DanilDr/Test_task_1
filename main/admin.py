'''
Created on 05.07.2013
'''

# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import Followers

class FollowersAdmin(admin.ModelAdmin):
    list_display = ('name', 'numfollower', 'numpursuers')
    ordering = ('name',)
    class Media:
        css = {'all' : ['/static/css/test.css',]}
        js = ['/static/js/test.js',]

admin.site.register(Followers, FollowersAdmin)

