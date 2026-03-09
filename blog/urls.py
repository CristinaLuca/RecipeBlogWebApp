from django.urls import path
from . import views

urlpatterns = [
     path('blogList/', views.BlogListView.as_view(), name = "blogListView"),

     path('<slug:slug>/tag/', views.RecordTagView.as_view(), name='blogPost-tag'),


     path("<slug:slug>/<str:date>/", views.BlogDetailView.as_view(), name = 'blog'),
     path("<slug:slug>/", views.BlogDetailView.as_view(), {"date": "29/02/2024"}, name = 'blog'),
     path("<slug:slug>/", views.BlogDetailView_withMixin.as_view(), name='blog_detail'),
     
]
