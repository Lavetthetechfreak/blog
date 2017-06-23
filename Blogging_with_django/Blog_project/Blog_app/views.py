from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
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
		instance.save()
		#message success
	#messages.success(request, "content Created succesfully")
	#return HttpResponseRedirect(instance.get_absolute_url())
	#if request.method=="POST":
		#print request.POST.get('title')
		#print request.POST.get('content')
		
	context = {
	 'form': form,
	}
	return render(request, 'create.html',context)
	#message success
	messages.success(request, "content Created succesfully")
	return HttpResponseRedirect(instance.get_absolute_url())
	
#else:
	#essages.error(request, "content error")

	#return HttpResponse('<h1>Hello this is my create</h1>')
def details(request, id=None):
	instance = get_object_or_404(Blog,id=id)
	context ={
		"instance":instance,
	}
	return render(request, 'details.html',context)

def update(request, id=None):

	instance = get_object_or_404(Blog,id=id)
	form = BlogForm( request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Item saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context ={
		"instance":instance,
		"form":form,
	}

	return render(request, 'create.html',context)

	
	
def delete(request, id=None):
	instance = get_object_or_404(Blog,id=id)
	instance.delete()
	return redirect("posts:list")
	messages.success(request, "Item deleted")
	
