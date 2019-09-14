from django.urls import path
from . import views

urlpatterns = [
    path('registeraccount/', views.register_user, name='account-create'),
    path('login/', views.login_user, name='account-login'),
    path('logout/', views.logout_user, name='account-logout')
]