from django.shortcuts import render, HttpResponse

def blog1(request):
    return render(request, 'blog/html/blog1.html')
