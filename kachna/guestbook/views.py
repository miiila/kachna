from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post


def index(request):
    posts = Post.objects.order_by('-timestamp')
    context = {'posts': posts}
    return render(request, 'guestbook/index.html', context)

def add(request):
    post = Post()
    if request.user:
        post.author_name = request.user.get_full_name()
        post.author_email = request.user.email
    else:
        post.author_name = request.POST['author_name']
        post.author_email = request.POST['author_email']
    post.text=request.POST['text']
    post.save()

    return HttpResponseRedirect(reverse('guestbook:index'))
