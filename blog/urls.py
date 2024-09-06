from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView
)

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), # maps to model-name_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # uses same template as create
    path('about/', views.about, name='blog-about'),
]