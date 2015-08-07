from django import forms
from django.db import IntegrityError
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Profile, Image, WallPost, WallPost, Comment
from .forms import CreateUserForm, ProfileForm, UploadImageForm, MakeWallPostForm
from .utils import normalize_query, get_query

# Create your views here.
def index(request):
	if request.user.is_authenticated():
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
	if request.user.is_authenticated():
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
	else:
		form = CreateUserForm()
	return render(request, "social/register.html", {
		'form': form,
	})

def home(request):
	if not request.user.is_authenticated():
		# redirects to index page
		return HttpResponseRedirect(reverse("social:index"))
	avatar = None
	try:
		avatar = request.user.profile.image_set.get(is_avatar=True)
	except Image.DoesNotExist:
		pass
	if request.method == 'POST':
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
	if not request.user.is_authenticated():
		# redirects to index page
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
	if not request.user.is_authenticated():
		# redirects to index page
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
	if not request.user.is_authenticated():
		# redirects to index page
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
	if not request.user.is_authenticated():
		# redirects to index page
		return HttpResponseRedirect(reverse("social:index"))
	avatar = None
	user = User.objects.get(pk=user_id)
	try:
		avatar = user.profile.image_set.get(is_avatar=True)
	except Image.DoesNotExist:
		pass
	if request.method == 'POST':
		form = MakeWallPostForm(request.POST)
		if form.is_valid():
			new_post = form.save()
	form = MakeWallPostForm(initial={"profile": user_id, "poster_id": request.user.id, 'poster_username': request.user.username, })
	return render(request, "social/profile.html", {
		'avatar': avatar,
		'user': user,
		'form': form,
	})

def make_comment(request, user_id):
	user = User.objects.get(pk=user_id)
	post = request.POST.get('post', '')
	post_id = WallPost.objects.get(pk=post)
	comment_text = request.POST.get('comment_text', '')
	if comment_text:
		Comment.objects.create(post=post_id, poster_id=request.user.id, poster_username=request.user.username, comment_text=comment_text)
	return HttpResponseRedirect(reverse("social:profile", kwargs={'user_id': user.id,}))

def search(request):
	if not request.user.is_authenticated():
		# redirects to index page
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

def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect(reverse("social:index"))