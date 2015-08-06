import datetime
import random
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	fb_id = models.BigIntegerField(verbose_name="Facebook User ID", null=True, blank=True, unique=True)
	RELIGION_CHOICES = (
		('Christian', 'Christian'),
		('Sinner (other)', 'Sinner (other)'),
		('Super Sinner (Atheist)', 'Super Sinner (Atheist)'),
	)
	religion = models.CharField(max_length=22, choices=RELIGION_CHOICES, default='Christian')
	bio = models.TextField(max_length=200, null=True, blank=True)

	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)

class Image(models.Model):
	profile = models.ForeignKey(Profile)

	def make_pic_dir(instance, filename):
		return '%s/%s' % ('images', str(uuid.uuid4()) + '.' + filename.split('.')[-1])
		
	pic = models.ImageField(upload_to=make_pic_dir)