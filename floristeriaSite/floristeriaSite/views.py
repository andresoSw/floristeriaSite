from django.shortcuts import render

def home(request):
	template = 'floristeriaSite/home.html'
	context = {}
	return render(request,template,context)

def index(request):
	template = 'floristeriaSite/index.html'
	context = {}
	return render(request,template,context)
