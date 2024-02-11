from django.shortcuts import render

def p0(request):
    return render(request, "portfolio/html/portfolio_firstpage.html")
def p1(request):
    return render(request, "portfolio/html/p1.html")
