from django.urls import path
from . import views 

urlpatterns = [
    path('api/',views.couple_create_read),
    path('api/<int:pk>/',views.couple_update_delete),
]
