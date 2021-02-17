from django.urls import path
from . import views 

urlpatterns = [
   path('',views.lead, name='lead'),
   path('screen2/', views.screen2, name='screen2'), 
   path('screen3/', views.screen3, name='screen3'),
   path('screen2/', views.PersonListView.as_view(), name='person_changelist'),
   path('screen2/add/', views.PersonCreateView.as_view(), name='person_add'),
   path('screen2/<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),

]
