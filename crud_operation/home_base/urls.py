from django.urls import path, include
from home_base import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('sign_out/', views.sign_out, name="sign_out"),
]
