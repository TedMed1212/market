from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('о программе/', views.about, name='about'),
    path('личный кабинет/', views.account, name='account')
]
