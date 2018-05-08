from django.conf.urls import url
from django.urls import path
from . import views

# 如果你忘了在 blog\urls.py 中添加app_name='blog'这一句，接下来你可能会得到一个 NoMatchReversed 异常
app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'post/', views.detail, name='detail'),

]