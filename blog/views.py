from django.shortcuts import render, render_to_response

# Create your views here.
from blog.models import Blog


def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html', {'blogs': blog_list})
