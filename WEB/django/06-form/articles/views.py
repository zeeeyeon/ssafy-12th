from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/update.html', context)


# def new(request):
#     # 게시글 작성 페이지 응답
#
#     # form instance 생성
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'articles/create.html', context)
#
#
# def create(request):
#     # 1. ModelForm instance 생성, 사용자 입력 데이터를 통째로 인자로 작성
#     form = ArticleForm(request.POST)
#
#     # 2. 유효성 검사(내부적으로 유효성 검사를 모두 진행)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#
#     # 유효성 검사 실패 후 내역을 담아서 보여줌
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/create.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    # request method is not POST
    # DB와 관련 되지 않은 코드
    else :
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else :
        form = ArticleForm(request.POST, instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# def edit(request, pk):
#     # 어떤 게시글을 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     # context = {
#     #     'article': article,
#     # }
#     # 글 수정 시 인스턴스로 기존 데이터 넣어주기
#     form = ArticleForm(instance=article)
#     context = {
#         'form': form,
#         'article': article,
#     }
#
#     return render(request, 'articles/edit.html', context)
#
#
# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#
#     # 1. 모델폼 인스턴스 생성(사용자 입력 데이터 + 기존 데이터)
#     form = ArticleForm(request.POST, instance=article)
#
#     # 2. 유효성 검사
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#
#     context = {
#         'form': form,
#         'article': article,
#     }
#     return render(request, 'articles/edit.html', context)