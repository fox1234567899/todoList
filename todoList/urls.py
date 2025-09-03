"""
URL configuration for todoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Post import urls 
from myapp import urls  
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(('myapp.urls', 'myapp'), namespace='myapp')),
    path('post/', include(('Post.urls', 'Post'), namespace='Post')),
        path('reset_password/',auth_views.PasswordResetView.as_view(template_name="passwordview.html",html_email_template_name='passwordemail.html'),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="passworddone.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="passwordconfirm.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="passwordcomplete.html"),name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
