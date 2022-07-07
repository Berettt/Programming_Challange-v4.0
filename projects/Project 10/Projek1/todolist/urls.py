from django.urls import path
from .views import todolist, update, delete



app_name = "todolist"

urlpatterns = [
    path('',todolist,name='aplikacja to do list'),
    path('update/<str:pk>/',update,name='taskupdate'),
    path('delete/<str:pk>/',delete,name='delet')
]