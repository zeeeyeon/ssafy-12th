from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # 직렬화
        # all() -> 다중 데이터 옵션은 many=True
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # elif를 사용하여 명시하는 것을 권장함
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # partial -> 부분 업데이트를 위한 파라미터, False로 지정시 모든 필드를 요구함
        # serializer 모든 필수 필드에 대한 값을 전달 받기 때문
        article = ArticleSerializer(data=request.data, instance=article, partial=True)

        if article.is_valid():
            article.save()
            return Response(article.data)
        return Response(article.errors, status.HTTP_400_BAD_REQUEST)