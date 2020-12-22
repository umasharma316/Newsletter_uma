from django.urls import path
from . import views


urlpatterns = [
    path('edition_1_2021/', views.edition_1_2021_home, name='edition_1_2021_home'),
    path('edition_1_2021/content_tech', views.edition_1_2021_content_tech, name='edition_1_2021_content_tech'),
    path('edition_1_2021/content_non_tech', views.edition_1_2021_content_non_tech, name='edition_1_2021_content_non_tech'),
    path('edition_1_2021/content_book', views.edition_1_2021_content_book, name='edition_1_2021_content_book'),
    path('edition_1_2021/images', views.edition_1_2021_images, name='edition_1_2021_images')
]