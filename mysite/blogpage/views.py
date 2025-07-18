
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from blogpage.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag
from blogpage.froms import Commentform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect




# Create your views here.
def blog_view(request, author_username=None, cat_name=None, tag_name=None):
    all_tags = Tag.objects.all()
    now = timezone.now()

    # فیلتر پیش‌فرض: فقط پست‌های منتشرشده و فعال
    posts = Post.objects.filter(published_date__lte=now, status=True)

    # فیلتر بر اساس آدرس
    if author_username:
        posts = posts.filter(author__username=author_username)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name])

    # صفحه‌بندی
    paginator = Paginator(posts, 3)  # نمایش ۳ پست در هر صفحه
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "posts": page_obj,
        "all_tags": all_tags,
    }

    return render(request, 'blog/blog-home.html', context)



def blog_single(request,pid):
    if request.method=='POST':
        print('============request.method================')
        form = Commentform(request.POST)
        if form.is_valid():
            form.save()
            print('============save================')
            messages.add_message(request, messages.SUCCESS, "Comment saved successfully.after approve with admin you can see it")
        else:
            messages.add_message(request, messages.ERROR, "Comment don't saved !")
   
    now = timezone.now()
    post=get_object_or_404(Post,pk=pid,published_date__lte=now,status=True)
    next_post = Post.objects.filter(id__gt=post.id,published_date__lte=now,status=True).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=post.id,published_date__lte=now,status=True).order_by('-id').first()
    print('============show================',request.method)
    if not post.login_require:
        comments=Comment.objects.filter(post=post.id,approve=True)
        form=Commentform()
        post.counted_views += 1
        post.save()
        return render(request, 'blog/blog-single.html', {
                'post': post,
                'next_post': next_post,
                'prev_post': prev_post,
                'comments':comments,
                'form':form,
        })
    else:
        if  request.user.is_authenticated:
            comments=Comment.objects.filter(post=post.id,approve=True)
            form=Commentform()
            post.counted_views += 1
            post.save()
            return render(request, 'blog/blog-single.html', {
                            'post': post,
                            'next_post': next_post,
                            'prev_post': prev_post,
                            'comments':comments,
                            'form':form,
                    })
        return HttpResponseRedirect(reverse('login'))
        
        #return redirect('/')


def blog_search(request):
    now=timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=True)
    if request.method == "GET":
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
        #posts=posts.filter(content__contains=request.GET.get('s'))
    
    context={"posts":posts}
    return render(request,'blog/blog-home.html',context)

