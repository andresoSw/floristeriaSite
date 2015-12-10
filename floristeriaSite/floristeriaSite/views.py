from django.shortcuts import render

def home(request):
	template = 'floristeriaSite/home.html'
	context = {}
	return render(request,template,context)
