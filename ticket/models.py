from django.db import models
from bttis.common_user.models import CommonUser

# Create your models here.
class List(models.Model):
    title = models.CharField('类型', max_length = 20, unique = True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['id']
    class Admin:
        pass
    
class Ticket(models.Model):
    trainNum = models.CharField('车次', max_length = 5)
    tickettype = models.ForeignKey(List, verbose_name = '类型')
    startStation = models.CharField('出发车站', max_length = 10)
    destination = models.CharField('到达车站', max_length = 10)
    date = models.DateField('日期')
    class Meta:
        ordering = ['-date']

import datetime
class TicketInfo(models.Model):
    infotype = models.CharField('车票类型', choices=(('in', '转让'), ('out', '求购')), max_length = 2)
    ticketNum = models.PositiveIntegerField('车票数量')
    ticket = models.ForeignKey(Ticket, verbose_name = '车票')
    phone = models.CharField('联系电话', max_length = 15)
    extraContext = models.TextField('其他说明')
    time = models.DateTimeField('发布时间', default = datetime.datetime.now)
    user = models.ForeignKey(CommonUser, verbose_name = '发布用户')
    class Meta:
        ordering = ['-time']
