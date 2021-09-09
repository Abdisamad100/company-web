from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('team/', views.my_photos, name='myPhotos'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('job/', views.job, name='job'),
]