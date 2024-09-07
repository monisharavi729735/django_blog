from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentDeleteView
)

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view() , name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), # maps to model-name_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # uses same template as create
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]