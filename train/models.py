from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField('类型', max_length = 20, unique = True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['title']
    class Admin:
        pass

class Train(models.Model):
    trainNum = models.CharField('车次', max_length = 5)
    traintype = models.ForeignKey(List, verbose_name = '类型')
    startStation = models.CharField('始发站', max_length = 10)
    startTime = models.TimeField('始发时间')
    destination = models.CharField('到达站', max_length = 10)
    desTime = models.TimeField('到站时间')
    endStation = models.CharField('终点站', max_length = 10)
    endTime = models.TimeField('终到时间')
    mileage = models.IntegerField('里程', default = 0)
    runTime = models.CharField('运行时间(xx<小时>xx<分钟>)', max_length = 4)
    hardSleeperPrice = models.IntegerField('硬卧票价', default = 0)
    hardSeatPrice = models.IntegerField('硬座/动车二等座票价', default = 0)
    softSleeperPrice = models.IntegerField('软卧票价', default = 0)
    softSeatPrice = models.IntegerField('软座/动车一等座票价', default = 0)
    def __unicode__(self):
        return self.trainNum
    class Meta:
        ordering = ['trainNum', 'mileage']
    class Admin:
        pass