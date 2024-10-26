from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from WorldOfSpeed.utils import get_user_obj
from cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from cars.models import Car


class CarCatalogueView(ListView):
    model = Car
    template_name = 'cars/catalogue.html'


# Create your views here.
class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('car_catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()

        return super().form_valid(form)


class CarDetailsView(DetailView):
    model = Car
    template_name = 'cars/car-details.html'
    pk_url_kwarg = 'id'


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = 'cars/car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('car_catalogue')


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'cars/car-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('car_catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
