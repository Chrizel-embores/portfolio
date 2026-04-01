# base/urls.py

from django.urls import path
from . import views   # <-- this imports from base/views.py

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),

]

