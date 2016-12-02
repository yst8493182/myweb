from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from blog.models import Blog, Book


def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html', {'blogs': blog_list})


@csrf_exempt
def login(request):
    blog_list = Blog.objects.all()
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    users_ = [username]
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/login_ok/')
        # response.set_cookie('username', username, 3600)
        request.session['username'] = users_
        return response

    else:
        return render_to_response('index.html', {'error': 'username or password error!', 'blogs': blog_list})


@login_required
def login_ok(request):
    blog_list = Blog.objects.all()
    # username = resquest.COOKIES.get("username", '')
    username = request.session.get("username", "")
    user = username[0]
    return render_to_response('login_ok.html', {'user': user, 'blogs': blog_list})


@login_required
def logout(request):
    response = HttpResponseRedirect('/index/')
    # response.delete_cookie('username')
    del request.session['username']
    return response


# 学生表
def student(request):
    books=Book.objects.all()
    student = {
        'jack': [22, 'boy', 'Programmer'],
        'alen': [27, 'boy', 'Designer'],
        'una': [23, 'girl', 'Tester'],
        'Brant': [23, 'girl', 'Tester'],
        'David': [23, 'boy', 'Tester']
    }
    return render_to_response("student.html", {"student_list": student,"book_list":books})
