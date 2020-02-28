from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    django 要求模型必须继承与models.Model 类
    Category 只需要一个简单的类目 name 就行
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """
    标签tag 也比较简单和 Category 一样,
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Post(models.Model):
    """
    文章的表格比较复杂啊
    """

    # 文章标题比较简单实用Char
    title = models.CharField('标题',max_length=70)
    # 文章的正文使用 TextField
    body = models.TextField('正文')
    # 创建时间 时间类型
    create_time = models.DateTimeField('创建时间',default= timezone.now)
    # 修改时间
    modified_time = models.DateTimeField('修改时间')
    # 摘要, 默认是必须要输入的, 添加 blank 以后可以为nil
    excerpt = models.CharField('摘要',max_length=200, blank=True)

    # category, 一篇文章只有一个分类, 一个分类下面可以有多个文章, 是一对多的关系
    # ForeignKey 标示的是一个一对多的关系, ForeignKey 必须传入一个 on_delete 参数用来指定当关联的
    # 据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=models.CASCADE)

    # tag, 一篇文章可以有多个 标签, 并且是可以为空的
    tag = models.ManyToManyField(Tag,verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.modified_time = timezone.now()
        super().save()

        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('TestModel:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = '文章'
        #verbose_name_plural 多篇文章同时时用负数的形式
        verbose_name_plural = verbose_name
