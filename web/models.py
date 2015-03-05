# encoding: utf-8
from django.db import models

# Create your models here.


class CATEGORY(models.Model):
    name = models.CharField(u'分类名', max_length=32)


class TORRENT(models.Model):
    name = models.CharField(u'名称', max_length=128)
    content = models.BinaryField(u'文件内容')
    category = models.ForeignKey(CATEGORY)