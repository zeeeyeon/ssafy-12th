from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

# 과거 catch
def create(request):
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2.1, 필드가 많을 경우 객체에 값을 주기 힘듦
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2.2, 유효성 검사를 통과 해야 save() 진행 -> 이 방법 채택
    article = Article(title=title, content=content)
    article.save()

    #2.3, 유효성 검사(저장 전 검사 진행)를 진행할 타이밍이 존재하지 않음
    # article = Article.objects.create(title=title, content=content)


    # 3. 추출 한 입력 데이터를 활용하여 DB에 저장 요청
    return render(request, 'articles/detail.html', {})
