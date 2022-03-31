"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from music_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music_app.urls')) # указываем на другую папку где есть наши url




    # path('music/', MusicListView.as_view()), # Если класс указываем as_view()
    # path('music-create/', MusicCreateView.as_view()),
    # path('music-update/<int:pk>/', MusicUpdateView.as_view()), # указываем какую именно id обновить
    # path('music-detail/<int:pk>/', MusicDetailView.as_view()),# указываем какую именно id вытащить
    # path('music-delete/<int:pk>/', MusicDeleteView.as_view()),# указываем какую именно id удалить

    # path('music/', get_music),
    # # path('category/', get_category)
    # path('music/<int:id>/', music_detail),
    # path('music-create/', music_create),
]
