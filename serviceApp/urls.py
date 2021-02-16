from django.urls import path
from . import views 

urlpatterns = [
   path('',views.lead, name='lead'),
   path('screen2/', views.screen2, name='screen2'), 
   path('screen3/', views.screen3, name='screen3'), 
]
