from django.shortcuts import render,get_object_or_404
# from django.core.paginator import Paginator
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog_type,Blog,User


# 博客首页列表
def blog_list(request):
    # 博客分类
    blog_types=Blog_type.objects.all()
    # 作者分类
    authors=User.objects.all()
    blogs=Blog.objects.filter(is_delete=False)
    # 总共博客数量，相当于Blog.objects.filter(is_delete=False).count()
    blogs_nums=blogs.count()
    # 分页功能的实现
    try:
        page=request.GET.get('page',1)
    except PageNotAnInteger:
        page=1
    p=Paginator(blogs,3,request=request)
    blogs_page=p.page(page)
    # return render(request,'blog_list.html',{'blogs':blogs})
    return render(request,'blog/blog_list.html',{'blogs':blogs,'blogs_nums':blogs_nums,
                                                'blog_types':blog_types,'authors':authors})


# 博客详情页
def blog_detail(request,blog_pk):
    blog=get_object_or_404(Blog,pk=blog_pk)
    # 博客上一篇文章、下一篇文章
    pre_blog=Blog.objects.filter(id__gt=blog.id).order_by('id')
    next_blog=Blog.objects.filter(id__lt=blog.id).order_by('-id')

    # 只去查询出来的第一条数据
    if pre_blog.count()>0:
        pre_blog=pre_blog[0]
    else:
        pre_blog=None

    if next_blog.count()>0:
        next_blog=next_blog[0]
    else:
        next_blog=None

    return render(request,'blog/blog_detail.html',{'blog':blog,'pre_blog':pre_blog,'next_blog':next_blog})


# 对应分类下的所有博客列表(点击分类显示该分类下的所有博客)
def blogs_with_type(request,blog_type_pk):
    # 根据传入的ID查询出来所属分类(用于博客分类页面的title显示取值,以及分类页面分类：公司公告(总共有3篇博客))
    blog_type=get_object_or_404(Blog_type,pk=blog_type_pk)
    # 再根据所属分类的id，找出此类id下面的所有博客文章
    # blogs=Blog.objects.filter(blog_type=blog_type) 另一种取值方式
    blogs=Blog.objects.filter(blog_type=blog_type_pk)
    # 用于获取进入分类页面的‘博客分类’显示
    blog_types=Blog_type.objects.all()
    # 用域获取进入作者分类页面的‘作者分类’显示
    authors=User.objects.all()
    return render(request,'blog/blogs_with_type.html',{'blogs':blogs,'blog_types':blog_types,'authors':authors,'blog_type':blog_type})


# 对应作者下的所有博客列表(点击作者显示该作者的所有博客)
def blogs_with_author(request,blog_author_pk):
    # 根据传入的作者ID查询出来作者(用于作者分类页面title显示取值,以及作者页面的作者：谢霆锋(总共有2篇博客))
    blog_author=get_object_or_404(User,pk=blog_author_pk)
    blogs=Blog.objects.filter(author=blog_author_pk)
    # 用于获取进入分类页面的‘博客分类’显示
    blog_types=Blog_type.objects.all()
    # 用域获取进入作者分类页面的‘作者分类’显示
    authors=User.objects.all()
    return render(request,'blog/blogs_with_author.html',{'blogs':blogs,'blog_types':blog_types,'authors':authors,'blog_author':blog_author})



