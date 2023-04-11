from django.urls import path, include
from class_base import views

urlpatterns = [
    path('', views.c_add.as_view(), name="c_add"),
    path('delete/<int:id>/', views.c_delete.as_view(), name="c_delete"),
    path('<int:id>/', views.c_update.as_view(), name="c_update"),
]
