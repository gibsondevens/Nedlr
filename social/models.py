import uuid

from django.db import models
from django.contrib.auth.models import User

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
	bio = models.TextField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)

class Image(models.Model):
	profile = models.ForeignKey(Profile)

	def make_pic_dir(instance, filename):
		""" creates a random string to use as the new name for uploaded images
			then appends it with the filetype of the original
		"""
		return '%s/%s' % ('images', str(uuid.uuid4()) + '.' + filename.split('.')[-1])
		
	pic = models.ImageField(upload_to=make_pic_dir)
	is_avatar = models.BooleanField(default=False)

class WallPost(models.Model):
	profile = models.ForeignKey(Profile)
	poster_id = models.IntegerField()
	poster_username = models.CharField(max_length=20)
	post_text = models.TextField(max_length=200, verbose_name='Write wall post')

class Comment(models.Model):
	post = models.ForeignKey(WallPost)
	poster_id = models.IntegerField()
	poster_username = models.CharField(max_length=20)
	comment_text = models.CharField(max_length=200, verbose_name='Write comment')