from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import * 
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {
        'index':'/',
        'all-data':'/all-data/',
        'one-data':'/one-data/id',
        'create-data':'/create-data',
        'delete-data':'/delete-data/id',
        'edit-data':'/edit-data/id',
    }
    return Response(api_urls)

@api_view(['GET'])
def all_data(request):
    uid=User.objects.all()
    serializer =UserSerializers(uid,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def one_data(request,pk):
    uid=User.objects.get(id=pk)
    serialize=UserSerializers(uid)
    return Response(serialize.data)

@api_view(['GET','POST'])
def create_data(request):
    if request.method == "POST":
        serialize=UserSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
        return Response(serialize.data)
    else:
        data = {
        "username":"username",
        "email":"email"
    }
    return Response(data)

@api_view(['GET','DELETE'])
def delete_data(request,pk):
    if request.method == "DELETE":
        try:
            uid=User.objects.get(id=pk)
            uid.delete()
            return Response("delete data")
        except:
            return Response('Invalid Id')
    else:
        try:

            uid = User.objects.get(id=pk)
            serializer = UserSerializers(uid)
            return Response(serializer.data)
        except:
            return Response('Data not found')  
        
@api_view(['GET','PUT'])
def edit_data(request,pk):
    uid=User.objects.get(id=pk)
    if request.method == "PUT":
        serialize=UserSerializers(instance=uid,data=request.data)
        if serialize.is_valid():
            serialize.save() 
    serializer=UserSerializers(uid) 
    return Response(serializer.data)
  