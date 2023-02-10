from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {'text': title}
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Группа № {slug}')


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {'text_2' : title}
    return render(request, template, context)
