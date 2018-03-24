from django.shortcuts import render

# Create your views here.


def register(request):
    """进入注册界面"""
    return render(request, 'register.html')
