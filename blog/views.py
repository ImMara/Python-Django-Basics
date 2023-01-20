from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def article(request, numero_article):
    try:
        return render(request, f"blog/article-{numero_article}.html", {'numero_article': numero_article})
    except:
        return render(request, 'blog/article-not-found.html', {})
