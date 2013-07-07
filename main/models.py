# -*- coding: utf-8 -*-

from django.db import models


class Followers(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя")
    follow_ids = models.TextField(blank=True, null=True, verbose_name="ID преследуемых")
    pursuers = models.TextField(blank=True, null=True, verbose_name="ID преследователей")
    #numpersecuted = models.IntegerField(default=0, verbose_name='Количество преследуемых')
    #numpursuers = models.IntegerField(default=0, verbose_name='Количество преследователей')
    class Meta:
        db_table = u"man_man"
        ordering = ['id', ]
    def __unicode__(self):
        return self.name
    def numfollower(self): # количество преследуемых
        return FollowerFollower.objects.filter(id_follower = self.id).count()
    def numpursuers(self): # количество преследователей
        return FollowerFollower.objects.filter(id_pursuers = self.id).count()
    def save(self, *args, **kwargs):
        list_folowers = self.follow_ids.split(' ')
        FollowerFollower.objects.filter(id_follower=self.id).delete()
        [FollowerFollower.objects.get_or_create(id_follower=self.id, id_pursuers = int(follower)) 
            for follower in list_folowers if follower.isdigit()]
        
        list_pursuers = self.pursuers.split(' ')
        FollowerFollower.objects.filter(id_pursuers=self.id).delete()
        [FollowerFollower.objects.get_or_create(id_follower=pursuer, id_pursuers = int(self.id)) 
            for pursuer in list_pursuers if pursuer.isdigit()]
        
        super(Followers, self).save(*args, **kwargs)

class FollowerFollower(models.Model):
    id_follower = models.IntegerField(blank=True, null=True) # преследователь
    id_pursuers = models.IntegerField(blank=True, null=True) # преследуемый
    def __unicode__(self):
        return u"%s - %s" % (self.id_follower, self.id_pursuers)
