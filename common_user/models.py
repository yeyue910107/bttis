from django.db import models

# Create your models here.
class CommonUser(models.Model):
    userName = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.userName
    class Admin:
        pass