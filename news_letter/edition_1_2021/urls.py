from django.urls import path
from . import views


urlpatterns = [
    path('edition_1_2021/', views.edition_1_2021_home, name='edition_1_2021_home')
]