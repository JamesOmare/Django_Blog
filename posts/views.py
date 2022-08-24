from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post


def index(request:HttpRequest):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def greet(request:HttpRequest):
    name = request.GET.get('name') or 'World'
    return HttpResponse(f'Hello {name}')


def return_all_posts(request:HttpRequest):
    # return HttpResponse(str(posts))
    pass


def return_one_post(request:HttpRequest, post_id):
    # for post in posts:
    #     if post['id'] == post_id:
    #         return HttpResponse(str(post))
        
    #     return HttpRequest('Not Found')
    pass

def create_post(request):
    form = PostCreationForm()
    
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('posts_home')

    context = {
        'form': form
    }
    return render(request, 'create_post.html' ,context)

def post_detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    image_url = post.thumbnail

    context = {
        'post': post,
        'image_url' : image_url
    }
    return render(request, 'post_detail.html', context)

def update_post(request, post_id):
    post_to_update = Post.objects.get(pk = post_id)
    form = PostCreationForm(instance = post_to_update)

    if request.method == 'POST':
        form = PostCreationForm(instance = post_to_update,
                                data = request.POST,
                                files = request.FILES)

        if form.is_valid():
            form.save()

            return redirect('posts_home')

    context = {
        'form': form
    }
    return render(request, 'update.html', context)