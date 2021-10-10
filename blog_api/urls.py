from django.urls import path
from .vews import PostList,PostDetail
app_name='blog_api'

urlpatterns=[
    path('<int:pk>/',PostDetail.as_view(),name='detailcreatel'),
    path('',PostList.as_view(),name='listcreate'),
    
    
]
