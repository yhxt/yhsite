from django.db import models
from django.contrib.auth.models import User


class Blog_type(models.Model):
    type_name=models.CharField(max_length=15,verbose_name=u'分类名')

    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'标题')
    blog_type=models.ForeignKey(Blog_type,on_delete=models.DO_NOTHING)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    last_update_time=models.DateTimeField(auto_now=True,verbose_name=u'修改时间')
    is_delete=models.BooleanField(default=False,verbose_name=u'是否删除')

    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

