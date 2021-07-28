
from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ),
    path('reponse/<str:msg>',views.getResponse ),
]
