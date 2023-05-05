from rest_framework import serializers
from. import models
from djgram.users.models import User as user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_model
        fields=("id", "username", "profile_photo",)
        

class CommentSerializer(serializers.ModelSerializer):
    author=AuthorSerializer()
    class Meta :
        model=models.Comment
        fields=("id", "contents","author")


class PostSerializer(serializers.ModelSerializer):
    comment_post=CommentSerializer(many=True)
    author=AuthorSerializer()
    # image = serializers.ImageField(use_url=True)
    class Meta :
        model=models.Post
        fields=("id", "image", "caption", "author", "comment_post", "image_likes")



