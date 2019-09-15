from django.urls import path
from . import views

urlpatterns = [
    path('getratings/', views.get_all_data, name='data-getratings'),
    path('submitrating/', views.submit_rating, name='data-newrating'),
    path('getgoodtimes/', views.get_good_times, name='data-goodtimes')
]