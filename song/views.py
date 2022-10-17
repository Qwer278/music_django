from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect
from .models import Song, User, Like

global user_data, page_object


def home(request):
    return render(request, "login.html")


def index(request):
    if (request.GET):
        like_value = request.GET['value']
        title = request.GET['title']
        try:
            if like_value == 'like':
                Like.objects.filter(username=request.user, song_title=title).update(is_like='False')
            elif like_value == 'dislike':
                Like.objects.filter(username=request.user, song_title=title).update(is_like='True')
        except:
            Like.objects.create(username=request.user, song_title=title, is_like=True)
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {"page_obj": page_object}
    return render(request, "index.html", context)


def login(request, username=None, password=None):
    if request.POST:
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, 'login.html')
        user_obj = User.objects.filter(username=username).values()
        if request.GET:
            like_value = request.GET['value']
            title = request.GET['title']
            try:
                if like_value == 'like':
                    Like.objects.filter(username=request.user, song_title=title).update(is_like='False')
                elif like_value == 'dislike':
                    Like.objects.filter(username=request.user, song_title=title).update(is_like='True')
            except:
                Like.objects.create(username=request.user, song_title=title, is_like=True)
        paginator = Paginator(Song.objects.all(), 1)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        user_data = {"user_obj": user_obj, "page_obj": page_object}
        return user_data


def signuplogin(request):
    print(request.method)
    if request.method == "POST":
        user = request.POST['Username']
        pas = request.POST['password']
        user_obj = User.objects.create(username=user, password=pas)
        user_obj.save()
        usera = authenticate(request, username=user, password=pas)
        login(request, usera)
        user_obj = User.objects.filter(username=user).values()
        print(request.method)
        if (request.POST):
            print('GET DONE')
            like_value = request.POST['value']
            title = request.POST['title']
            print(like_value, title)
            try:
                if like_value == 'like':
                    Like.objects.filter(username=request.user, song_title=title).update(is_like='False')
                elif like_value == 'dislike':
                    Like.objects.filter(username=request.user, song_title=title).update(is_like='True')
            except:
                Like.objects.create(username=request.user, song_title=title, is_like=True)
        paginator = Paginator(Song.objects.all(), 1)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        user_data = {"user_obj": user_obj, "page_obj": page_object}
        return render(request, 'index.html', user_data)
    else:
        return render(request, "login.html")


def user_login(request):
    if request.POST:
        username = request.POST['Username']
        password = request.POST['password']
        usera = authenticate(username=username, password=password)
        login(request, usera)
        user_obj = User.objects.filter(username=username).values()
        like_obj = Like.objects.filter(username=request.user).values()
        if (request.GET):
            try:
                like_obj = Like.objects.filter(username=request.user).values()
            except:
                like_obj = Like.objects.create(username=request.user, is_like=True)
            like_obj = {'like_obj': like_obj}
        paginator = Paginator(Song.objects.all(), 1)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        user_data = {"user_obj": user_obj, "page_obj": page_object}
        return render(request, 'index.html', user_data)
    else:
        return render(request, "user_login.html")


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, "login.html")
