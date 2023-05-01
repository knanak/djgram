from django.shortcuts import render, get_object_or_404
from djgram.users.models import User as user_model

from . import models

# Create your views here.
def index(request):
    return render(request, 'posts/base.html')

def post_create(request):
    if request.method == 'GET':
        return render(request, 'posts/create.html')
    
    elif request.mothod == 'POST':
        if request.user.is_authenticated:
            user=get_object_or_404(user_model, pk=request.user_id)
            image=request.FILES['image']
            caption=request.POST['caption']

            new_post=models.Post.objects.create(
                author=user,
                image=image,
                caption=caption
            )
            new_post.save()
            return render(request, 'posts/base.html')

        else : return render(request, 'users/main.html') ## 로그인 확인 안되면, 로그인 페이지로

                