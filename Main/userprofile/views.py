from django.shortcuts import render

def profile(request):
    return render(request, 'portfolio__page.html')