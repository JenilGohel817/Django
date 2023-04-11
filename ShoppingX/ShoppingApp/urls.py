from django.urls import path, reverse_lazy
from ShoppingApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordForm, mypasswordreset, Mysetpassword

urlpatterns = [
    path('', views.ProductView.as_view(), name="index"),
    path('product_details/<int:pk>', views.ProductDetailView.as_view(), name='product_details'),


    path('adminpanel/', views.admin, name='adminpanel'),
    # path('', views.index, name='index'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),

    path('orders/', views.orders, name='orders'),

    path('topwear', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    path('bottomwear', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),

    path('signup/', views.CustomerReg.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('mobile', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('profile/', views.ProflieView.as_view(), name='profile'),
    path('address/', views.address, name='address'),



    path('buy_now/', views.buy_now, name='buy_now'),
    path('checkout/', views.checkout, name='checkout'),

    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='showcart'),

    # path('product_details/<int:pk>', views.product_details, name='product_details'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html',  form_class=MyPasswordForm, success_url='/passwordchangedone/'), name='change_password'),

    path('password/', auth_views.PasswordResetView.as_view(template_name='passwordreset.html', form_class=mypasswordreset), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='passwordresetdone.html'), name='password_reset_done'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='passwordchangedone'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='passwordresertconfime.html',
                                                                                success_url='/pass-com/', form_class=Mysetpassword), name='password_reset_confirm'),

    path('registration/', views.CustomerReg.as_view(), name='CustomerReg'),

    path('pass-com/', auth_views.PasswordResetCompleteView.as_view(template_name='passcomplate.html'), name='pass-com'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
