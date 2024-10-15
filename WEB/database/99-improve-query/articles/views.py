from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count


# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    # 댓글의 갯수까지 포함해서 쿼리 날리기
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)


def index_2(request):
    # articles = Article.objects.order_by('-pk')
    # 게시글과 1:N 관계에 있는 1의 작성자를 가져오겠다.
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)


def index_3(request):
    # articles = Article.objects.order_by('-pk')
    # N의 관계에 있는 애들을 다 가져오겠다. (python이 내부적으로 가져와주는 query)
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)


from django.db.models import Prefetch


def index_4(request):
    # articles = Article.objects.order_by('-pk')

    # 게시글 + 게시글의 댓글 목록 => N을 가져오는 것 prefetch
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')

    # 게시글 + 댓글 목록 + 댓글의 작성자 => prefetch_related
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
