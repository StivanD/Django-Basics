from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.utils import get_user_obj
from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.models import Author


# Create your views here.
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard_page')


class AuthorDetailsView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author_details')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDeleteView(DeleteView):
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return get_user_obj()
