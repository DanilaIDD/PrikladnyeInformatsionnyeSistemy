from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # Если POST
            form = {
                'text': request.POST["text"], 
                'title': request.POST["title"]
            }
            # Заполнение полей
            if form["text"] and form["title"]:
                # Уникальность названия статьи
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Такая статья уже существует!"
                    return render(request, 'create_post.html', {'form': form})
                # Создание статьи
                article = Article.objects.create(
                    text=form["text"], 
                    title=form["title"], 
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
            else:
                # Если не все заполнено
                form['errors'] = "Заполните все поля!"
                return render(request, 'create_post.html', {'form': form})
        else:
            # Если GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404
