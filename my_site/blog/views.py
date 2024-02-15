from django.shortcuts import render, HttpResponse
from .models import *

def blog1(request):
    return render(request, 'blog/html/blog1.html')

def education(request):
    educations=Education.objects.all()
    context ={'university':educations}
    return render(request, 'blog/html/blog2.html', context)