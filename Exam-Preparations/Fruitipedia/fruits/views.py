from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from Fruitipedia.utils import get_user_obj
from fruits.forms import FruitEditForm, FruitCreateForm, FruitDeleteForm
from fruits.models import Fruit


# Create your views here.
class DashboardView(ListView):
    model = Fruit
    template_name = 'fruits/dashboard.html'


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard_page')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()

        return super().form_valid(form)


class FruitDetailsView(DetailView):
    model = Fruit
    pk_url_kwarg = 'id'
    template_name = 'fruits/details-fruit.html'


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    pk_url_kwarg = 'id'
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard_page')


class FruitDeleteView(DeleteView):
    model = Fruit
    form_class = FruitDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard_page')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)