from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def commands(request):
	return render(request, 'cmd.html', {})

def developers(request):
	return render(request, 'dev.html', {})

def privacy_p(request):
	return render(request, 'privacy.html',  {})

