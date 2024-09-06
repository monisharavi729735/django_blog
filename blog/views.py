from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based view, fewer lines of code if naming convention followed
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html for class based views
    context_object_name = 'posts'    # equivalent to context in fn views, default name = object
    ordering = ['-posted']      # newest to oldest
    

class PostDetailView(DetailView):
    model = Post
    # template_name = post_detail.html
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})