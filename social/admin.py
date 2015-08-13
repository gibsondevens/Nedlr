from django.contrib import admin

from .models import Profile, WallPost, Comment, Notification

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	fields = ['user', 'religion', 'bio', 'fb_id']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(WallPost)
admin.site.register(Comment)
admin.site.register(Notification)