from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomePage(ListView):
    http_method_names = ['get']
    template_name = 'feed/homepage.html'
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-id')[0:30]


class PostDetail(DetailView):
    http_method_names = ['get']
    template_name = 'feed/detail.html'
    model = Post
    context_object_name = 'post'


class CreateNewPost(CreateView):
    http_method_names = ['get', 'post']
    template_name = 'feed/create.html'
    model = Post
    fields = ['text']
