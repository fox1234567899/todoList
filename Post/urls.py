from django.urls import path
from .views import CreatePost,DeletePost,UpdatePost,PostList,PostDetail
app_name='Post'



urlpatterns = [
    path('create/',CreatePost.as_view(),name='create'),
    path('delete/<int:pk>',DeletePost.as_view(),name='delete'),
    path('update/<int:pk>',UpdatePost.as_view(),name='update'),
    path('list/',PostList.as_view(),name='list'),
    path('detail/<int:pk>',PostDetail.as_view(),name='detail'),
  


]
