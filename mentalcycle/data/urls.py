from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_all_data, name='data-user'),
    path('submitrating/', views.submit_rating, name='data-newrating')
]