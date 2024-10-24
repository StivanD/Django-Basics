from django.urls import path, include

from fruits import views

urlpatterns = [
    path('create/', views.FruitCreateView.as_view(), name='create_fruit'),
    path('<int:id>/', include([
        path('details/', views.FruitDetailsView.as_view(), name='fruit_details'),
        path('edit/', views.FruitEditView.as_view(), name='edit_fruit'),
        path('delete/', views.FruitDeleteView.as_view(), name='delete_fruit')
    ]))
]