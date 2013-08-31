from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField('类型', max_length = 250, unique = True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['title']
    class Admin:
        pass

import datetime 
class Item(models.Model):
    title = models.CharField('标题', max_length = 250)
    created_date = models.DateTimeField('发布时间', default = datetime.datetime.now)
    article = models.TextField('内容')
    article_list = models.ForeignKey(List, verbose_name = '类型')
    author = models.CharField('作者', max_length = 20)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-created_date', 'title']
    class Admin:
        pass