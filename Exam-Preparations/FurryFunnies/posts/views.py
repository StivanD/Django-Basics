from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.utils import get_user_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


# Create your views here.
class DashboardView(ListView):
    model = Post
    template_name = 'posts/dashboard.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard_page')

    def form_valid(self, form):
        form.instance.author = get_user_obj()

        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'id'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard_page')


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard_page')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)