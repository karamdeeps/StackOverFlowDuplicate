from django.urls import path, include
from django.contrib import admin
from .views import index, QuestionViewSet, fetch_questions, list
from rest_framework import routers


router = routers.DefaultRouter()
router.register("questions", QuestionViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
    path('list', list, name="list"),
    path('fetch_questions/', fetch_questions, name="latest_questions"),
]
