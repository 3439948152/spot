from django.urls import path,include
from .views import SPOTView,tagsView,buttonView
urlpatterns=[
    path('spot/',SPOTView.as_view()),
    path('tags/',tagsView.as_view()),
    path('',buttonView.as_view())
]