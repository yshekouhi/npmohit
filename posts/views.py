from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = Post.objects.filter(featured=False).order_by('created_at')
        context["featured_posts"] = Post.objects.filter(featured=True)
        context["top_post"] = Post.objects.get(top_post=True)
        return context
    context_object_name = 'post'    

class PostListView(ListView):
    template_name = 'posts/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = Post.objects.filter(featured=False).order_by('created_at')
        context["featured_posts"] = Post.objects.filter(featured=True)
        return context      

