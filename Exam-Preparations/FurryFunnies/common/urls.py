from django.urls import path

from common import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home_page')
]