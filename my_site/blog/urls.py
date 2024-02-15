from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog1, name='blog0'),
    path('blog2/', views.education, name='university'),

]
