# -*- coding: utf-8 -*-

from django.db import models
from django.db import connection

class Followers(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя")
    follow_ids = models.TextField(blank=True, null=True, verbose_name="ID преследуемых")
    numpersecuted = models.IntegerField(default=0, verbose_name='Количество преследуемых')
    numpursuers = models.IntegerField(default=0, verbose_name='Количество преследователей')
    class Meta:
        db_table = u"man_man"
        ordering = ['id', ]
    def __unicode__(self):
        return self.name
    def save(self, parent=False, *args, **kwargs):
        listpersecuted = [int(idf) for idf in self.follow_ids.split(' ') if idf.isdigit()]
        self.numpersecuted = len(listpersecuted) # запись количества преследуемых
        sqlstr = r"select * from man_man where follow_ids like %s or follow_ids like %s or follow_ids like %s"
        cursor = connection.cursor()
        cursor.execute(sqlstr, ['% ' + str(self.id) + ' %', '% ' + str(self.id), str(self.id) + ' %' ]) # sql запрос по поиску преследователей
        self.numpursuers = len(cursor.fetchall())  # запись количества преследователей
        super(Followers, self).save(*args, **kwargs)
        if parent == False:
            querypersecuted = Followers.objects.filter(id__in=listpersecuted)
            for follower in querypersecuted:
                follower.save(parent=True)
        else:
            pass


        