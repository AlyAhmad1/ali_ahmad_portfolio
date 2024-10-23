from django.shortcuts import render, HttpResponse


def portfolio_index(request):
    return render(request, 'index.html')
