from django.urls import path
from . import views


urlpatterns = [
    path('edition_1_2021/', views.edition_1_2021_home, name='edition_1_2021_home'),
    path('edition_1_2021/content', views.edition_1_2021_content, name='edition_1_2021_content'),
    path('edition_1_2021/images', views.edition_1_2021_images, name='edition_1_2021_images')
]