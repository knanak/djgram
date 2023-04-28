from django.urls import path
# from djgram.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )
from . import views

app_name = "users"
urlpatterns = [
    path('', views.main, name='main')
]
