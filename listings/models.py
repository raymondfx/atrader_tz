from django.db import models
from datetime import datetime
from counsellors.models import Counsellor

class Listing(models.Model):
  counsellor = models.ForeignKey(Counsellor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title