from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm

def home_page(request):
    posts = News.objects.all().order_by('-date')[:4]
    context = {'posts': posts}
    return render(request, './index.html', context)

def news_page(request):
    posts = News.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, './news-list.html', context)

def details_page(request, pk):
    post = get_object_or_404(News, pk=pk)
    context = {'post': post}
    return render(request, './news-detail.html', context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
    else:
        form = NewUserForm()

    context = {'form': form}
    return render(request, './sign-up.html', context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, './login.html', context)

def logout_request(request):
    logout(request)
    return redirect("home_page")