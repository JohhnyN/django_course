from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('web-design-3/', views.web_design_3, name='web-design-3'),
    path('devops/', views.devops, name='devops'),
    path('restaurant-manager/', views.restaurant_manager, name='restaurant-manager'),
    path('excel-gsheets/', views.excel_gsheets, name='excel-gsheets'),
    path('music-manager', views.music_manager, name='music-manager'),
]
