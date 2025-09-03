from django.urls import path
from .views import Homepage,LoginPage,SignUp,ProfilePage
from django.contrib.auth.views import LogoutView


app_name='myapp'



urlpatterns = [
    path('',Homepage.as_view(),name='index'),
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('profile/',ProfilePage.as_view(),name='profile'),


]
