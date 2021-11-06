
from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Post
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from blogApp.forms import PostForm

from django.urls import reverse_lazy
# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blogs/post-list.html'

class PostDetail(DetailView):
    model = Post
    
    template_name = 'blogs/post-detail.html'

class add_post_view(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/add-post.html'
    #fields = '__all__'

class UpdateDetailView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/update-post.html'

    #fields = ['blog_title', 'blog_author', 'blog_date', 'blog_read_time', 'blog_tag', 'blog_content']

class DeleterDetailView(DeleteView):
    model = Post
    template_name = 'blogs/delete-post.html'
    success_url = reverse_lazy('post-list')