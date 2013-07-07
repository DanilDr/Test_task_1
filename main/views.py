# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from main.models import Followers, FollowerFollower
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def initdb(request):
#    try:
    allfollowers = Followers.objects.all()
    for follower in allfollowers:
        [FollowerFollower.objects.create(id_follower=follower.id, id_pursuers = int(pursuers)) 
            for pursuers in follower.follow_ids.split(' ') if pursuers.isdigit()]
    return HttpResponse('Complete')
#    except:
#        return HttpResponse('Fail')

@login_required(login_url='/')
def getFolowersPursuers(request):
    name = request.GET.get('name')
    curfollowerid = Followers.objects.get(name = name).id # id текущего
    
    followers_id = FollowerFollower.objects.filter(id_follower=curfollowerid) # id преследуемых

    pursuers_id  = FollowerFollower.objects.filter(id_pursuers=curfollowerid)# id преследователей
    
    persons_list = [{'id' : pers.id, 'name' : pers.name} for pers in Followers.objects.all().order_by('name')]
    pursued_list = [pursued.id_pursuers for pursued in followers_id]
    pursuers_list = [pursuers.id_follower for pursuers in pursuers_id]
    
    reqjson = [persons_list,pursued_list, pursuers_list]
    return HttpResponse(json.dumps(reqjson))