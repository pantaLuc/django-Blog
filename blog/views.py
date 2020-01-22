from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='blog/home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='blog/post_new.html'
    fields='__all__'
class BlogUpdateView(UpdateView):
    model=Post
    fields=['title','body']
    template_name='blog/post_edit.html'

class BlogDeleteView(DeleteView):
    model=Post
    template_name='blog/post_delete.html'
    success_url=reverse_lazy('home')