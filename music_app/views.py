from email.policy import HTTP

from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from music_app.models import Music, Category
from music_app.serializers import MusicSerializer


# @api_view(['GET'])
# def get_music(request):
#     """Get all music"""
#     musics = Music.objects.all()
#     serializer = MusicSerializer(musics, many=True)
#     # print("****************************")
#     # print(musics)
#     # print("****************************")
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def music_detail(request, id):
#     try:
#         music = Music.objects.get(id=id)
#         serializer = MusicSerializer(music, many=False)
#         return Response(serializer.data)
#     except Music.DoesNotExist:
#         raise Http404
#
#
# @api_view(['POST'])
# def music_create(request):
#     # print("++++++++++++++++++++++++++++++")
#     # print(request.data)
#     # print("++++++++++++++++++++++++++++++")
#     # print(dir(request))
#     # print("++++++++++++++++++++++++++++++")
#     serializer = MusicSerializer(data=request.data) # десерилизация для БД
#     if serializer.is_valid(): # все ли данные указали,все ли серилизовали; проверяет на правильность
#         serializer.save() # записывает информацию в базу данных
#         return Response(serializer.data, status=status.HTTP_201_CREATED) # выводит созданную инФОРМАЦИЮ а так же статус
#     else:
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MusicListView(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicCreateView(CreateAPIView):
    serializer_class = MusicSerializer


class MusicUpdateView(UpdateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDetailView(RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDeleteView(DestroyAPIView):
    # lookup_field = 'id' # указываем что будет работать с id а не с pk
    queryset = Music.objects.all()
    serializer_class = MusicSerializer



# @api_view(['GET'])
# def get_category(request):
#     category = Category.object.all()
#     serializer = CategorySerializer(category, many=True)
#     return Response(serializer.data)
#
#
#
#

