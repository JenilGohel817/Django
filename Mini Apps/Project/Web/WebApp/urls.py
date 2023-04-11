from django.urls import path
from django import views
from WebApp import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('Indexx/', views.Indexx, name='Indexx'),
    path('<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
