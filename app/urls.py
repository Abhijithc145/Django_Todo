from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Delete/<str:pk>',views.Delete,name='Delete'),
]