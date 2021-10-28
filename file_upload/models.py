from django.db import models
import pdb

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)

class Csv(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  contact = models.BigIntegerField(null=True)

  @classmethod
  def create_data(cls, list):
    data = []
    for l in list:
      data.append(l)
    cls.objects.bulk_create(list)   