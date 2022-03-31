from django.urls import path

from music_app.views import *

urlpatterns = [
    path('music/', MusicListView.as_view()), # Если класс указываем as_view()
    path('music-create/', MusicCreateView.as_view()),
    path('music-update/<int:pk>/', MusicUpdateView.as_view()), # указываем какую именно id обновить
    path('music-detail/<int:pk>/', MusicDetailView.as_view()),# указываем какую именно id вытащить
    path('music-delete/<int:pk>/', MusicDeleteView.as_view()),# указываем какую именно id удалить

    # path('music/', get_music),
    # # path('category/', get_category)
    # path('music/<int:id>/', music_detail),
    # path('music-create/', music_create),
]
