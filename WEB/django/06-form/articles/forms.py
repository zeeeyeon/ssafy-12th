from cProfile import label

from django import forms
from .models import Article

# class ArticleForm(forms.Form):
    # 컬럼 중복 작성하기 시루미 => ModelForm 사용하기
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                # 'class': 'px-5, mt-5',
                'class': 'form-control',
                'placeholder': 'Enter article title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter article content',
                'rows': 10,
                'cols': 20,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'}
    )

    # Meta
    class Meta:
        model = Article
        # magic method 활용
        # fields = '__all__'

        # 제외하고 싶은 목록
        # exclude = ('title',)

        # 추가하고 싶은 목록
        fields = ('title',)