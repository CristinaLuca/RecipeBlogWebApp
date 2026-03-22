from django.urls import path

from . import views
from .views import TagCreateView

urlpatterns = [
    
    path('homepage_v1/', views.homepage_v1, name = "homepage_v1"),
    path('homepage_v1_withStyle/', views.homepage_v1_withStyle, name = "homepage_v1_withStyle"),
    path('homepage_v2/', views.homepage_v2, name = "homepage_v2"),
    path('homepage_v4/', views.Homepage_v4.as_view(), name = "homepage_v4"),
    path('homepage_Inheritance/', views.homepage_Inheritance, name = "homepage_Inheritance"),

    path('inputTag_v1/', views.inputTag_v1, name = 'inputTag_v1'),
    path('inputTagManual/', views.inputTag_manual, name = 'inputTagManual'),
    path('inputTag/', views.inputTag_manual, name = 'inputTag'),

    path("createTag/", TagCreateView.as_view(), name="tag_create"),
]