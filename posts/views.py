from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views import View

# second way to add login required decorator a CreatePost class based view
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator


class HomePage(View):

    template_name = 'index.html'

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'posts': page_obj
        }
        return render(request, self.template_name, context)


class About_Page(HomePage):
    template_name = 'about.html'

# def index(request:HttpRequest):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'index.html', context)

# def about(request):
#     return render(request, 'about.html')

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

@method_decorator(login_required, 'dispatch')
class CreatePost(View):
    template_name = 'create_post.html'
    form_class = PostCreationForm
    initial_values = {

    }
        
    #Another way of using decorator
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(CreatePost, self).dispatch(request, *args, **kwargs)
    

    def get(self, request):
        form = self.form_class(initial = self.initial_values)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('posts_home')



# @login_required
# def create_post(request):
#     form = PostCreationForm()
    
#     if request.method == 'POST':
#         form = PostCreationForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()

#             return redirect('posts_home')

#     context = {
#         'form': form
#     }
#     return render(request, 'create_post.html' ,context)

def post_detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    image_url = post.thumbnail

    context = {
        'post': post,
        'image_url' : image_url
    }
    return render(request, 'post_detail.html', context)

@login_required
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