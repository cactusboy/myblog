from django.shortcuts import get_object_or_404, render
# from django.http import  HttpResponse
from .models import Post
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # 显示所有文章，order_by是排序，-created_time是按创建时间倒序排列
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post':post})