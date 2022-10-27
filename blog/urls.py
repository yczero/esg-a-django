from django.urls import path
from blog import views

urlpatterns = [

    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    path('new/', views.post_new),
    path('restaurants/', views.res_index),
    path('restaurants/new/', views.res_new),
    path('restaurants/<int:pk>/', views.single_rest_page),
]