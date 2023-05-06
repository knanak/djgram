from django.urls import path
from . import views

app_name='posts'

urlpatterns=[
    path('', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/post_update/', views.post_update, name='post_update'),
    path('<int:post_id>/post_like/', views.post_like, name='post_like'),
    path('<int:post_id>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:cmt_id>/comment_delete/', views.comment_delete, name='comment_delete'),
]


