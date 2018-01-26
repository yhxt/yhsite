from django.contrib import admin
from django.urls import path,include
from blog import views
from yhsite import views

urlpatterns = [
    path('', views.home,name='home'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
]
