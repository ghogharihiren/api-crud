from django.urls import path
from .views import*



urlpatterns = [
     path('', ArticleView.as_view()),
     path('update/<int:pk>',Articleviews.as_view())
]