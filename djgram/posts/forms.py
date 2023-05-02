from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta :
        model=Post
        fields=['caption', 'image']
        labels = {'caption': '설명', 'image':'이미지'}
        