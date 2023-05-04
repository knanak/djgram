from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from djgram.users.models import User as user_model
from django.db.models import Q
from django.urls import reverse

from . import models, serializers
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated :
            user=get_object_or_404(user_model, pk=request.user.id)
            following = user.following.all()
            posts=models.Post.objects.filter(Q(author__in = following) | Q(author=user))
            comment_form=CommentForm()
            serializer=serializers.PostSerializer(posts, many=True)
            return render(request, 'posts/main.html', 
                          {'posts' : serializer.data, 
                           'comment_form': comment_form})

def post_create(request):
    if request.method == 'GET':
        form=CreatePostForm()
        return render(request, 'posts/create.html', {'form':form})
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            user=get_object_or_404(user_model, pk=request.user.id)
            form=CreatePostForm(request.POST, request.FILES)   # 장고form에 post에서 가져온 데이터를 바로 넣을 수
            
            if form.is_valid():
                post=form.save(commit=False)
                post.author=user
                post.save()
            else : print(form.errors)

            # image=request.FILES['image']
            # caption=request.POST['caption']

            # new_post=models.Post.objects.create(
            #     author=user,
            #     image=image,
            #     caption=caption
            # )
            # new_post.save()
            return HttpResponseRedirect(reverse('posts:index'))

        else : return render(request, 'users/main.html') ## 로그인 확인 안되면, 로그인 페이지로


def post_update(request, post_id):
    if request.user.is_authenticated:

        post=get_object_or_404(models.Post, pk=post_id)
        if request.user != post.author :
            redirect(reverse('posts:index'))

        if request.method == 'GET':
            form=UpdatePostForm(instance=post)
            return render(request, 'posts/post_update.html', {'form':form, 'post':post})
            
    else : redirect(reverse('users:main'))

def comment_create(request, post_id):
    if request.user.is_authenticated:
        post=get_object_or_404(models.Post, pk=post_id)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse('posts:index') + '#comment-' + str(comment.id))
        

        else : return render(request, 'users/main.html')


def comment_delete(request, cmt_id):
    if request.user.is_authenticated:
        comment=get_object_or_404(models.Comment, pk=cmt_id)
        if request.user == comment.author :
            comment.delete()
        return redirect(reverse('posts:index'))
    else :
        return render(request, 'users/main.html')