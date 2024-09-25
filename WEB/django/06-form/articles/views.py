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
    return render(request, 'articles/detail.html', context)


def new(request):
    # 게시글 작성 페이지 응답

    # form instance 생성
    form = ArticleForm()
    context = {
        'form': form,
    }

    return render(request, 'articles/new.html', context)


def create(request):
    # 1. ModelForm instance 생성, 사용자 입력 데이터를 통째로 인자로 작성
    form = ArticleForm(request.POST)

    # 2. 유효성 검사(내부적으로 유효성 검사를 모두 진행)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)

    # 유효성 검사 실패 후 내역을 담아서 보여줌
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    # 어떤 게시글을 수정할지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 1. 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)
    # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 3. 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    article.title = title
    article.content = content
    # 4. 저장
    article.save()

    return redirect('articles:detail', article.pk)