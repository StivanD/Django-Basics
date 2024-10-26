from django.urls import path, include

from cars import views

urlpatterns = [
    path('catalogue/', views.CarCatalogueView.as_view(), name='car_catalogue'),
    path('create/', views.CarCreateView.as_view(), name='create_car'),
    path('<int:id>/', include([
        path('details/', views.CarDetailsView.as_view(), name='car_details'),
        path('edit/', views.CarEditView.as_view(), name='edit_car'),
        path('delete/', views.CarDeleteView.as_view(), name='delete_car')
    ]))
]
