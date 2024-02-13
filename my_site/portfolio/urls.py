from django.urls import path
from . import views

urlpatterns = [
    path('', views.p0, name='portfolio0'),
    path('p1/', views.p1,  name='portfolio1')
]
