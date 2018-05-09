from django.conf.urls import url
from django.urls import path
from . import views

# 如果你忘了在 blog\urls.py 中添加app_name='blog'这一句，接下来你可能会得到一个 NoMatchReversed 异常
app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'post/(?P<pk>[0-9] +)/$', views.detail, name='detail'),
    path(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    path(r'category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]