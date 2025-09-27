from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
@login_required
def create_post(request):
    if request.method == "POST":
        form = {
            'text': request.POST["text"], 
            'title': request.POST["title"]
        }
        if form["text"] and form["title"]:
            if Article.objects.filter(title=form["title"]).exists():
                form['errors'] = "Такая статья уже существует!"
                return render(request, 'create_post.html', {'form': form})
            article = Article.objects.create(
                text=form["text"], 
                title=form["title"], 
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = "Заполните все поля!"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Проверка на заполненность полей
        if not (username and email and password and confirm_password):
            return render(request, 'register.html', {
                'error': 'Заполните все поля!',
                'username': username,
                'email': email
            })
        # Проверка совпадения паролей
        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Пароли не совпадают!',
                'username': username,
                'email': email
            })
        # Проверка уникальности имени пользователя
        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {
                'error': 'Пользователь с таким именем уже существует!',
                'username': '',
                'email': email
            })
        except User.DoesNotExist:
            # Создание пользователя
            user = User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('archive')
    return render(request, 'register.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Проверка на заполненность полей
        if not (username and password):
            return render(request, 'login.html', {
                'error': 'Заполните все поля!',
                'username': username
            })
        # Аутентификация пользователя
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {
                'error': 'Неверное имя пользователя или пароль!',
                'username': username
            })
    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('archive')
