from django.shortcuts import render, get_object_or_404
from .models import Project, Blog

def home_view(request):
    projects = Project.objects.all().order_by('-created_at')[:6]  # most recent first
    return render(request, 'projects/home.html', {'projects': projects})


def projects_view(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/projects.html', {'projects': projects})


def blogs_view(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'projects/blogs.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'projects/blog_detail.html', {'blog': blog})
