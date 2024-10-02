from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#  Django는 User 모델을 직접 참조하는 것을 권장하지 않는다. / 아래의 직접 참조로 사용하지 않기(유지 보수가 힘들어짐)
# from .models import User

# 그래서 Django는 User 모델을 간접적으로 참조할 수 있는 방법을 별도로 제공한다.
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    # UserCreationForm 상속 받기
    class Meta(UserCreationForm.Meta):
        #  Django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
        model = get_user_model()

class CustomUserChangeForm(UserCreationForm):
    # password가 안뜨게 설정
    # password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')