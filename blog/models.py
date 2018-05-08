from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# python_2_unicode_compatible 装饰器用于兼容 Python2

# Create your models here.


@python_2_unicode_compatible  # python3不加这个装饰器不会受到影响
class Category(models.Model):  # 分类
    name = models.CharField(max_length=100)

    # 使用__str__可以返回实际的数据而不是数据的数量
    def __str__(self):
        return self.name


class Tag(models.Model):  # 标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):  # 文章表
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    created_time = models.DateTimeField()
    # 文章最后一次修改时间
    modified_time = models.DateTimeField()
    # 文章摘要,可以为空
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类字段关联分类表，用外键一对多的关系
    # 当一个model对象的ForeignKey关联的对象被删除时，默认情况下此对象也会一起被级联删除的
    # ForeingKey外键必须加on_delete参数
    category = models.ForeignKey(Category, on_delete=True)
    #  标签字段关联标签表，用多对多的外键,并且可以为空
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者，也就是用户，从django.contrib.auth.models导入
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、
    # 登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 一篇文章只有一个作者，所以用一对多外键关联django的内置User表
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


