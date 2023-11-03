from .views import *
from django.urls import path

urlpatterns = [
    #path('<slug:slug>/',PostDetail.as_view(),name='post_detail'),
    
    path('comments/',comments,name='comments_data'),
    path('login/',login),
    path('signup/',signup),
    path('',PostList.as_view(), name='home'),
    path('<slug:slug>/',post_detail,name='post_detail'),
    
]
