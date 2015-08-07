from django.contrib import admin

from .models import Profile, WallPost, Comment

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	fields = ['user', 'religion', 'bio', 'fb_id']

admin.site.register(Profile, ProfileAdmin)