from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path(r'comment/post/(?P<post_pk>[0-9]+)/s', views.post_comment, name='post_comment'),
]