from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    Data = Post.objects.all()
    paginator = Paginator(Data,3)
    page_number = request.GET.get('page')
    data_final = paginator.get_page(page_number)
    template_name = 'blog/index.html'
    blog = Blog.objects.all().first
    featured_post = Post.objects.filter(featured=True)[:4]
    story_post = Post.objects.filter(featured=False)
    context = {'blog':blog,'featured_post':featured_post,'story_post':story_post,'data':data_final}
    return render(request, template_name, context)


def single_view(request,slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post':post}
    return render(request,'blog/post.html', context)