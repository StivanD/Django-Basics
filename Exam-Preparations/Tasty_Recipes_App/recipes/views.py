from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from TastyRecipes.utils import get_user_obj
from recipes.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes.models import Recipe


# Create your views here.
class CatalogueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user_obj()

        return super().form_valid(form)


class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    pk_url_kwarg = 'id'


class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = 'recipes/edit-recipe.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')


class RecipeDeleteView(DeleteView):
    model = Recipe
    form_class = RecipeDeleteForm
    template_name = 'recipes/delete-recipe.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
