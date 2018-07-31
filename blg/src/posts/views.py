from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post


def post_create(request):
	context={
	"title":"Create"
	}
	return render(request,"index.html",context)

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
	return render(request,"index.html",context)

def post_update(request):
	context={
	"title":"Update"
	}
	return render(request,"index.html",context)

def post_delete(request):
	context={
	"title":"Delete"
	}
	return render(request,"index.html",context)