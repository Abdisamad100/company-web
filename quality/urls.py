from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('team/', views.my_photos, name='myPhotos'),
    path('about/', views.about, name='about'),
]