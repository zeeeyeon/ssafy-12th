import random
from lib2to3.fixes.fix_input import context

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'zeeyeon'
    }
    return render(request, 'index.html', context)

def dinner(request):
    foods = ['국밥', '피자', '햄버거', '고기']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked': picked
    }
    return render(request, 'dinner.html', context)

def search(request):
    return render(request, 'search.html')

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # 사용자가 요청 보낸 데이터를 추출해서 context 딕셔너리에 세팅
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'catch.html', context)

def greeting(request, name):
    context = {
        'name' : name
    }
    return render(request, 'greeting.html', context)