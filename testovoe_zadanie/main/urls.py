
from django.urls import path 
from . import views

urlpatterns = [

   path('', views.index),
   path('id<int:number>', views.about)
]