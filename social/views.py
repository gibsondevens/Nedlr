import datetime

from django import forms
from django.db import IntegrityError
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Profile, Image, WallPost, WallPost, Comment, Notification
from .forms import CreateUserForm, ProfileForm, UploadImageForm, MakeWallPostForm
from .utils import normalize_query, get_query

# Create your views here.
def index(request):
	""" tries to log you in using your facebook by first checking if the facebook button returned a value
		if it does it checks that against the users in the db
		if it doesn't it will try to login with your username and password
	"""
	if request.user.is_authenticated():
		# redirects to home if user is signed in
		return HttpResponseRedirect(reverse("social:home"))
	if request.method == 'POST':
		fb_id = request.POST.get('fb_id', '')
		if fb_id:
			try:
				profile = Profile.objects.get(fb_id=fb_id)
				user = profile.user
				user.backend = 'django.contrib.auth.backends.ModelBackend'
				auth.login(request, user)
				return HttpResponseRedirect(reverse("social:home"))
			except Profile.DoesNotExist:
				return render(request, "social/index.html", {
					'error_message' : 'It seems like your Facebook is not linked to a Nedlr account. Please log in or register and link your accounts to use Facebook login.',
				})
		else:
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				# Correct password, and the user is marked "active"
				auth.login(request, user)
				# Redirect to a user profile.
				return HttpResponseRedirect(reverse("social:home"))
			else:
				# Show an error message
				return render(request, "social/index.html", {
					'error_message' : 'Your username or password was not correct. Please re-enter your credentials and try again.',
				})
	return render(request, "social/index.html")
	
def register(request):
	""" takes your form info and creates a user
		also creates a blank profile for that user
	""" 
	if request.user.is_authenticated():
		# redirects to home if user is signed in
		return HttpResponseRedirect(reverse("social:home"))
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			Profile.objects.create(user=new_user)
			return HttpResponseRedirect(reverse("social:index"))
		else:
			# Show an error message
			return render(request, "social/register.html", {
				'form' : form,
				'error_message' : 'The information you entered is not valid. Please re-enter and try again.',
			})
	form = CreateUserForm()
	return render(request, "social/register.html", {
		'form': form,
	})

def home(request):
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	avatar = None
	# set to none initially so that no errors are raised when it tries to load your profile pic
	try:
		avatar = request.user.profile.image_set.get(is_avatar=True)
		# tries to pull your profile pic
	except Image.DoesNotExist:
		pass
	if request.method == 'POST':
		# takes the value pulled from facebook and saves it to your profile
		fb_id = request.POST.get('fb_id', '')
		if fb_id:
			request.user.profile.fb_id = fb_id
			try:
				request.user.profile.save()
			except IntegrityError:
				return render(request, "social/home.html", {
					'avatar': avatar,
					'error_message' : 'It looks like that Facebook account is already linked to one of your neighborinos.'
				})
			return render(request, "social/home.html", {
				'avatar': avatar,
				'success_message' : 'Your Facebook is now linked with your Nedlr account.'
			})
		else:
			return render(request, "social/home.html", {
				'avatar': avatar,
				'error_message' : 'It looks like we did not receive any information from Facebook.'
			})
	return render(request, "social/home.html", {
		'avatar': avatar
	})

def change_profile(request):
	# replaces data in the user profile which by default is mostly blank
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			new_profile = form.save()
			return HttpResponseRedirect(reverse("social:home"))
		else:
			# Show an error message
			return render(request, "social/profile_change.html", {
				'form' : form,
				'error_message' : 'The information you entered is not valid. Please re-enter and try again.',
			})
	form = ProfileForm(instance=request.user.profile)
	return render(request, "social/profile_change.html", {
		'form': form,
	})

def upload_photo(request):
	# uses form to upload images as well as loading the users images so they don't upload them again
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	pics = request.user.profile.image_set.all()
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			new_pic = form.save()
			return HttpResponseRedirect(reverse("social:home"))
		else:
			return render(request, "social/photos.html", {
				'form' : form,
				'pics': pics,
				'error_message' : 'The picture you entered is not valid. Please try again.',
			})
	form = UploadImageForm(initial={"profile": request.user.profile})
	return render(request, "social/photos.html", {
		'form' : form,
		'pics': pics,
	})

def set_avatar(request):
	""" loops through all user images and sets none of them as the profile pic
		then sets the selected one as the profile pic
	""" 
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	if request.method == 'POST':
		pics = request.user.profile.image_set.all()
		for x in pics:
			x.is_avatar = False
			x.save()
		pic_id = request.POST.get('avatar', '')
		avatar = request.user.profile.image_set.get(pk=pic_id)
		avatar.is_avatar = True
		avatar.save()
		return HttpResponseRedirect(reverse("social:home"))

def profile(request, user_id):
	""" loads the users data and images based on their primary key value
		also uses form to make wall posts
	"""
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	avatar = None
	user = User.objects.get(pk=user_id)
	pics = user.profile.image_set.all()
	try:
		avatar = user.profile.image_set.get(is_avatar=True)
	except Image.DoesNotExist:
		pass
	if request.method == 'POST':
		form = MakeWallPostForm(request.POST)
		if form.is_valid():
			new_post = form.save()
			Notification.objects.create(user=user, notif_type='Wall Post', notif_text='Some one has posted on your Wall', notif_date=timezone.now())
	form = MakeWallPostForm(initial={"profile": user_id, "poster_id": request.user.id, 'poster_username': request.user.username, })
	return render(request, "social/profile.html", {
		'avatar': avatar,
		'user': user,
		'form': form,
		'pics': pics,
	})

def make_comment(request, user_id):
	# adds comments to wall post then returns the user to the profile
	user = User.objects.get(pk=user_id)
	post = request.POST.get('post', '')
	post_id = WallPost.objects.get(pk=post)
	comment_text = request.POST.get('comment_text', '')
	if comment_text:
		Comment.objects.create(post=post_id, poster_id=request.user.id, poster_username=request.user.username, comment_text=comment_text)
		Notification.objects.create(user=user, notif_type='Comment', notif_text='Someone has commented on your Wall Post', notif_date=timezone.now())
	return HttpResponseRedirect(reverse("social:profile", kwargs={'user_id': user.id,}))

def search(request):
	# uses the functions within utils.py to search based on the search form
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	query_string = ''
	results = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		user_query = get_query(query_string, ['first_name', 'last_name', 'username', 'email'])
		results = User.objects.filter(user_query)
	return render(request, 'social/search_results.html', {
		'query_string': query_string,
		'results': results
	}, context_instance=RequestContext(request))

def remove_notif(request):
	# uses the functions within utils.py to search based on the search form
	if not request.user.is_authenticated():
		# redirects to index page if user is not signed in
		return HttpResponseRedirect(reverse("social:index"))
	if request.method == 'POST':
		all_notifs = request.user.notification_set.all()
		all_notifs.delete()
	return HttpResponseRedirect(reverse("social:home"))

def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect(reverse("social:index"))