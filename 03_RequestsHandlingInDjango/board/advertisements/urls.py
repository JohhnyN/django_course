from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('advertisements/', views.Advertisements.as_view(), name='advertisements'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
]
