from django.urls import path

from . import views

urlpatterns = [
    
    path('homepage_v1/', views.homepage_v1, name = "homepage_v1"),
    path('homepage_v1_withStyle/', views.homepage_v1_withStyle, name = "homepage_v1_withStyle"),
    path('homepage_v2/', views.homepage_v2, name = "homepage_v2"),
    path('homepage_v4/', views.Homepage_v4.as_view(), name = "homepage_v2"),
    path('homepage_Inheritance/', views.homepage_Inheritance, name = "homepage_Inheritance"),
]