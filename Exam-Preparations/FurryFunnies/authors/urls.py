from django.urls import path

from authors import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='create_author'),
    path('details/', views.AuthorDetailsView.as_view(), name='author_details'),
    path('edit/', views.AuthorEditView.as_view(), name='edit_author'),
    path('delete/', views.AuthorDeleteView.as_view(), name='delete_author')
]