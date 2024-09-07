from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# class equivalent of @login-required, checks if creator == editor
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post, Comment

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
    paginate_by = 5
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html for class based views
    context_object_name = 'posts'    # equivalent to context in fn views, default name = object
    #ordering = ['-posted']      # newest to oldest
    paginate_by = 5
    
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted')

class PostDetailView(DetailView):
    model = Post
    # template_name = post_detail.html
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_content = request.POST.get('comment')
        if comment_content:
            post.comments.create(author=request.user, content=comment_content)
        return redirect('post-detail', pk=post.pk)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form): # to set the author for new post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        # Redirect to the post detail page after deletion
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})