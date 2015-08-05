import datetime
import random

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