from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Singer,Song
from . Serializers import  SingersSerializer,SongsSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

# class SingerViewSet(viewsets.ModelViewSet):
#     queryset = Singer.objects.all()
#     serializer_class = SingersSerializer

# class SongViewSet(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongsSerializer


# ====================other way to work nested serializer==========
@api_view()
def hello_world(request):
    return Response({"message":"Hello,World !"})


@api_view(["GET", "POST", "PUT"])
def get_singer(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            singer = Singer.objects.get(pk=pk)
            serializer = SingersSerializer(singer)
            return Response(serializer.data)
        else:
            singers_queryset = Singer.objects.all()
            serialized_data = SingersSerializer(singers_queryset, many=True)
            return Response({"singer_qureset": serialized_data.data})
    
    elif request.method == "POST":
        serializer = SingersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Singer created successfully."}, status=201)
        return Response(serializer.errors, status=400)


    elif request.method == "PUT":
        try:
            singer = Singer.objects.get(pk=pk)
        except Singer.DoesNotExist:
            return Response({"message": "Singer not found."}, status=404)

        serializer = SingersSerializer(singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Singer updated successfully."})
        return Response(serializer.errors, status=400)
    # ===============songs========

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def get_songs(request, pk=None):
    if request.method == 'GET':
        if pk:
            song = get_object_or_404(Song, pk=pk)
            serializer = SongsSerializer(song)
        else:
            songs = Song.objects.all()
            serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Song created successfully."}, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        song = get_object_or_404(Song, pk=pk)
        serializer = SongsSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Song updated successfully."})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        song = get_object_or_404(Song, pk=pk)
        song.delete()
        return Response({"message": "Song deleted successfully."}, status=204)