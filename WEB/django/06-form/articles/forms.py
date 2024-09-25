from django import forms
from .models import Article

# class ArticleForm(forms.Form):
    # 컬럼 중복 작성하기 시루미 => ModelForm 사용하기
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # Meta
    class Meta:
        model = Article
        # magic method 활용
        # fields = '__all__'

        # 제외하고 싶은 목록
        # exclude = ('title',)

        # 추가하고 싶은 목록
        fields = ('title',)