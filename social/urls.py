from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^home/$', views.home, name='home'),
	url(r'^home/update/$', views.change_profile, name='profile_change'),
	url(r'^home/upload/$', views.upload_photo, name='upload_photo'),
	url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
	url(r'^search/results/$', views.search, name='search'),
	url(r'^logout/$', views.logout, name='logout'),
]