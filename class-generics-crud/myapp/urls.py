from django.urls import path
from .views import*

urlpatterns = [
    path('',index,name='index'),
    path('data/',Userlistview.as_view()),
    # path('data/<int:id>',Userlistviews.as_view()),
    path('data/<int:pk>',Userlistviews.as_view()),
    
    

]