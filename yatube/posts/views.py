from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Group


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    return HttpResponse(f'Группа № {slug}')


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {'text_2': title}
    return render(request, template, context)
