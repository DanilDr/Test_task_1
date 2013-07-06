# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from main.models import Followers
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def initdb(request):
    try:
        followername = request.GET.get('name') 
        if followername:
            follower = Followers.objects.get(name=followername)
            follower.save()
        else:
            allfollowers = Followers.objects.all() # выборка всех преследователей
            for follower in allfollowers:
                follower.save() # сохрание преследовалетя
        return HttpResponse('Complete')
    except:
        return HttpResponse('Fail')

@login_required(login_url='/')
def getFolowers(request):
    allfolowers = Followers.objects.all().order_by('name') # выборка всех преследователей
    reqlist = [{'id' : folower.id, 'name' : folower.name} for folower in allfolowers]
    return HttpResponse(json.dumps(reqlist))