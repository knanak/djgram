from django.db import models
from djgram.users import models as user_model


class TimeStamp(models.Model):
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(TimeStamp):
    author=models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='post_author')
    image=models.ImageField(blank=True)
    caption=models.TextField(blank=True)
    image_likes=models.ManyToManyField(user_model.User, related_name='post_image_likes')


class Comment(TimeStamp):
    author=models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='comment_author')
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    comment=models.TextField(blank=True)