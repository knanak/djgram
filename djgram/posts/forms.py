from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta :
        model=Post
        fields=['caption', 'image']
        labels = {'caption': '설명', 'image':'이미지'}

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['caption']
        
class CommentForm(forms.ModelForm):
    contents=forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':78,}), label='')
    class Meta:
        model=Comment
        fields=['contents']