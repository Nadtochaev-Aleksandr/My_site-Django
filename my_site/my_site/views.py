from django.shortcuts import render, HttpResponse


def firstpage(request):
    return render(request, "html/firstpage.html")

# def firstpage(request):
#     return HttpResponse('Hi')