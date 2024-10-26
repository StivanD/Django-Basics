from django.urls import path, include

from recipes import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('<int:id>/', include([
        path('details/', views.RecipeDetailsView.as_view(), name='recipe_details'),
        path('edit/', views.RecipeEditView.as_view(), name='edit_recipe'),
        path('delete/', views.RecipeDeleteView.as_view(), name='delete_view')
    ]))
]