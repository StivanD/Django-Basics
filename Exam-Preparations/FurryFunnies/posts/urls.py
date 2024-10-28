from django.urls import path, include

from posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:id>/', include([
        path('details/', views.PostDetailsView.as_view(), name='post_details'),
        path('edit/', views.PostEditView.as_view(), name='edit_post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete_post')
    ]))
]