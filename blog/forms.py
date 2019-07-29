from django import forms
from .models import Portfolio, Comment


class NewBlog(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('가게명', '주소','사진')

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text','평점')