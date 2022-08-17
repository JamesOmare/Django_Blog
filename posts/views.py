from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

posts = [
    {
        'id':1,
        'title': 'Midnight Train',
        'author': 'James Lark'
    },

    {
        'id':2,
        'title': 'Midnight Thoughts',
        'author': 'James Lank'
    },

    {
        'id':3,
        'title': 'Midnight rain',
        'author': 'James Lore'
    },
   
]

def index(request:HttpRequest):
    name = request.GET.get('name') or 'World'
    context = {
        'name': name,
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
    return HttpResponse(str(posts))


def return_one_post(request:HttpRequest, post_id):
    for post in posts:
        if post['id'] == post_id:
            return HttpResponse(str(post))
        
        return HttpRequest('Not Found')