from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('list', Watch_List.as_view()),
    path('<int:pk>', Watch_Detail.as_view(),name='movie_detail'),
    path('stream',StreamPlatformAV.as_view()),
    path('stream/<int:pk>',StreamPlatform_Detail.as_view()),



    # path('review',ReviewList.as_view()),
    # path('review/<int:pk>',ReviewDetails.as_view()),

    path('stream/review/<int:pk>',ReviewList.as_view()),
    path('stream/<int:pk>/review',ReviewDetails.as_view()),   
    path('stream/<int:pk>/review-create',ReviewCreate.as_view()),




]
