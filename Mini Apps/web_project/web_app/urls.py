from unicodedata import name
from django.urls import path, include
from web_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('in', views.inX, name="in"),
    path('<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
