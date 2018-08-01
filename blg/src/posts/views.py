from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from .forms import PostForm
from .models import Post


def post_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	# if request.method == "POST":
	# 	print(request.POST.get("title"))
	# 	print(request.POST.get("content"))
	context={
	"form":form,
	"title":"Create"
	}
	return render(request,"post_form.html",context)

def post_detail(request, id=None): #retrive
	# instance = Post.objects.get(id=3)
	instance = get_object_or_404(Post, id=id)
	context={
	"title":instance.title,
	"instance":instance,
	}
	return render(request,"post_detail.html",context)

def post_list(request):
	queryset= Post.objects.all()
	context={
	"object_list":queryset,
	"title":"List"
	}
	return render(request,"post_list.html",context)

def post_update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form=PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"<a href='#'>Successfully</a> Edit", extra_tags="html_safe")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
	"title":instance.title,
	"instance":instance,
	"form":form,
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Successfully Delete")
	return redirect("posts:list")