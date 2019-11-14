from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(unique=True,null=False,max_length=20)
    upswd = models.CharField(max_length=20)