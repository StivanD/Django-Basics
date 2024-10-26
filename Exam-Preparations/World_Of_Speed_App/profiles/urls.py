from django.urls import path

from profiles import views

urlpatterns = [
    path('create', views.ProfileCreateView.as_view(), name='create_profile'),
    path('details/', views.ProfileDetailsView.as_view(), name='profile_details'),
    path('edit/', views.ProfileEditView.as_view(), name='edit_profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete_profile')
]