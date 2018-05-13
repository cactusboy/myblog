import markdown
from django.shortcuts import get_object_or_404, render
# from django.http import  HttpResponse
from comments.forms import CommentForm
from .models import Post, Category


# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # 显示所有文章，order_by是排序，-created_time是按创建时间倒序排列
    return render(request, 'blog/index.html', context={
        # 'title': '我的博客首页',
        # 'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得引入markdown模块
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    # 记得在顶部导入CommentForm
    form = CommentForm()
    # 获取这篇post下的全部评论
    comment_list = post.comment_set.all()

    # 将文章\表单\以及文章下的评论列表作为模板变量传给detail.html模板,以便渲染相应数据
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by("-created_time")
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    # 记得开始部分导入Category类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})