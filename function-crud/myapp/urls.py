from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all-data/',views.all_data,name='all-data'),
    path('one-data/<int:pk>',views.one_data,name='one-data'),
    path('create-data/',views.create_data,name='create-data'),
    path('delete-data/<int:pk>',views.delete_data,name='delete-data'),
    path('edit-data/<int:pk>',views.edit_data,name='edit-data')
    
    
]
