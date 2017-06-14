from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

# Create your views here.

def lists(request):
	obj = Blog.objects.all()
	context = {
		'lists' : obj,
	}
	return render (request, 'list.html',context)
def create(request):
	form = BlogForm( request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data('title')
		instance.save()
	#if request.method=="POST":
		#print request.POST.get('title')
		#print request.POST.get('content')
	context = {
	 'form': form,
	}
	return render(request, 'create.html',context)

	#return HttpResponse('<h1>Hello this is my create</h1>')
def details(request, id):
	instance = get_object_or_404(Blog,id=id)
	context ={
		"instance":instance,
	}
	return render(request, 'details.html',context)

def update(request):
	return HttpResponse('<h1>Hello this is my update</h1>')
def delete(request):
	return HttpResponse('<h1>Hello this is my delete</h1>')
