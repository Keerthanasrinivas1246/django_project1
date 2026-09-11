from django.urls import path
from base import views

urlpatterns = [
    #Genre
    path('create_genre/', views.create_genre, name='create_genre'),
    path('read_genre/', views.read_genre, name='read_genre'),
    path('update_genre/<int:pk>/', views.update_genre, name='update_genre'),
    path('delete_genre/<int:pk>/', views.delete_genre, name='delete_genre'), 

    #Article
    path('home/', views.home, name='home'),
    path('', views.read_article, name='read_article'),
    path('update_article/<int:pk>/', views.update_article, name='update_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),
    path('history_article/', views.history_article, name='history_article'),
    path('restore_article/<int:pk>/', views.restore_article, name='restore_article'),

    # <int:pk>/ ---> path converter
       
]