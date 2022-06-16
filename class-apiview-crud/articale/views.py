from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import * 
from .models import*
from django.contrib.auth.models import User


# Create your views here.
class ArticleView(APIView):
    def get(self,request):
        uid = Article.objects.all()
        serializer=ArticalSerializers(uid,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ArticalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data created"})
    
class Articleviews(APIView):
    
    def get(self,request,pk):
        uid=Article.objects.get(id=pk)
        serializer=ArticalSerializers(uid)
        return Response(serializer.data)
    
    
    def put(self,request,pk):
        uid=Article.objects.get(id=pk)
        serialize=ArticalSerializers(instance=uid,data=request.data)
        if serialize.is_valid():
            serialize.save()
        return Response({"data update"})
    
    def delete(self,request,pk):
        uid=Article.objects.get(id=pk)
        uid.delete()
        return Response({"deleted"})
        
        
    
    