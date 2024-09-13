from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def articles(request):
    return render(request, 'articles.html')