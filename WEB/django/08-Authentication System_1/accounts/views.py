from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        # form의 첫번째 인자는 request, 두번째는 data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 만약 인증된 사용자라면 로그인 진행(세션데이터 생성)
            # 인증된 유저 객체는 form에 저장되어 있음
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else :
        form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    # 세션 데이터 삭제
    auth_logout(request)
    return redirect('articles:index')