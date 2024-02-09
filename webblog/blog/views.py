from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):   # 'class base view' para lista de elementos de Django
    model = Post
    template_name = 'blog/index.html'# nombre por defecto del template= <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # nombre por defecto de obajetos= <object_list>
    ordering = ['-date_posted'] # el - invierte el ordenamiento de la fecha
    paginate_by = 5


class UserPostListView(ListView): 
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' 
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):   # el mixin se usa para requerir logueo a una class
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): # override de la validacion para aclarar el autor del post
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # se agrega mixin para que solo el author pueda editar
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): # override de la validacion para aclarar el autor del post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()    # obtiene el post que se desea actualizar
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()    # obtiene el post que se desea actualizar
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})