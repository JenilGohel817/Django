from django.urls import path, include
from function_base import views

urlpatterns = [
    path('', views.f_add, name="f_add"),
    path('delete/<int:id>/', views.f_delete, name="f_delete"),
    path('<int:id>/', views.f_update, name="f_update")
]
