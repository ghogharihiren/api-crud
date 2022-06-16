from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import*
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def index(request):
    api_rul={
        '':'index',
        'data':'data',
        'one-data':'data/id'
    }
    return Response(api_rul)


# class Userlistview(generics.GenericAPIView,
#                    mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin):
    
#     serializer_class=UserSerializer
#     queryset=User.objects.all()
#     lookup_field="id"
    
#     def get(self , request ,id=None):
#         if id:
#             return self.retrieve(request,id)
#         else:
#             return self.list(request)
    
#     def post(self , request):
#         return self.create(request)
    
#     def put(self,request ,id=None):
#         return self.update(request,id)   
    
#     def delete(self,request,id=None):
#         return self.destroy(request,id) 
    
class Userlistview(generics.ListCreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class Userlistviews(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()