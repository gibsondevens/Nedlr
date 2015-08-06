from django import forms
from django.db import IntegrityError
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Profile, Image
from .forms import CreateUserForm, ProfileForm, UploadImageForm

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
			return HttpResponseRedirect(reverse("social:index"), {
				'success_message' : 'You have succesfully created a profile. Please re-enter your credentials to log in.'
			})
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
		# redirects to index page and shows an error message
		return HttpResponseRedirect(reverse("social:index"))
	else:
		if request.method == 'POST':
			fb_id = request.POST.get('fb_id', '')
			if fb_id:
				request.user.profile.fb_id = fb_id
				try:
					request.user.profile.save()
				except IntegrityError:
					return render(request, "social/home.html", {
						'error_message' : 'It looks like that Facebook account is already linked to one of your neighborinos.'
					})
				return render(request, "social/home.html", {
					'success_message' : 'Your Facebook is now linked with your Nedlr account.'
				})
			else:
				return render(request, "social/home.html", {
					'error_message' : 'It looks like we did not receive any information from Facebook.'
				})
		return render(request, "social/home.html")

def change_profile(request):
	if not request.user.is_authenticated():
		# redirects to index page and shows an error message
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
	else:
		form = ProfileForm(instance=request.user.profile)
	return render(request, "social/profile_change.html", {
		'form': form,
	})

def upload_photo(request):
	if not request.user.is_authenticated():
		# redirects to index page and shows an error message
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
	else:
		form = UploadImageForm(initial={"profile": request.user.profile})
	return render(request, "social/photos.html", {
		'form' : form,
		'pics': pics,
	})

def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect(reverse("social:index"))