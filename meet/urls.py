from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('pick_a_date/', views.pick_a_date, name='pick_a_date'),
    path('success/', views.success, name='success'),
]
