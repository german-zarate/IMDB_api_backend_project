from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.http import HttpResponse
# Create your views here.



class StreamPlatformAV(APIView):


    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializers = StreamPlatform_serializer(platform,many=True,context={'request':request})
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = StreamPlatform_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class StreamPlatform_Detail(APIView):

    def get(self,request,pk):

        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'not found'},status=404)
        
        serializers = StreamPlatform_serializer(platform)
        return Response(serializers.data)
    
    def put(self,request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        data = request.data
        serializer = StreamPlatform_serializer(movie,data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
    

    def delete(self,request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return HttpResponse(status=204)






class Watch_List(APIView):

    def get(self,request):
        movie = WatchList.objects.all()
        serializers = WatchList_serializer(movie,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = WatchList_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)



class Watch_Detail(APIView):

    def get(self,request,pk):

        try:
            platform = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'not found'},status=404)
        
        serializers = WatchList_serializer(platform)
        return Response(serializers.data)
    
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        data = request.data
        serializer = WatchList_serializer(movie,data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
    

    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return HttpResponse(status=status.HTTP_302_FOUND)




# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = WatchList.objects.all()
#         serializers = WatchList_serializer(movie,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         data = request.data
#         serializer = WatchList_serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)
        

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     try:
#         movie = WatchList.objects.get(pk=pk)
#     except WatchList.DoesNotExist:
#         return Response(status=404)
    

#     if request.method == 'GET':
#         serializers = WatchList_serializer(movie)
#         return Response(serializers.data)
#     if request.method == 'PUT':
#         data = request.data
#         serializer = WatchList_serializer(movie,data=data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(serializer.errors)
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         movie.delete()
#         return HttpResponse(status=204)





