from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sale/', views.SalesAPIVIew.as_view(), name='sale')
]
