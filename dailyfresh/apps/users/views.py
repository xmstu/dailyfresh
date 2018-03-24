import re

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.users.models import User


def register(request):
    """进入注册界面"""
    return render(request, 'register.html')


def do_register(request):
    """处理注册逻辑"""

    # 获取请求参数(用户名,密码,确认密码,邮箱,勾选用户协议)
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    cpwd = request.POST.get('password2')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 校验参数合法性
    # 逻辑判断 0 0.0 '' None [] () {}  -> False
    # all: 所有的变量都为True, all函数才返回True, 否则返回False
    if not all([username, pwd, cpwd, email, allow]):

        print('*'*10)
        return render(request, 'register.html', {'message':'请填满所有参数'})

    # 判断两次输入的密码是否一致
    if pwd != cpwd:
        print('-' * 10)
        return render(request, 'register.html', {'message':'两次输入的密码不一致'})

    # 判断是否勾选了用户协议
    if allow != 'on':
        print('+' * 10)
        return render(request, 'register.html', {'message':'请先同意用户协议'})

    # 判断邮箱格式是否正确
    if not re.match('^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        print('/' * 10)
        return render(request, 'register.html', {'message': '邮箱格式不正确'})

    # 业务处理
    # 保存用户到数据库中
    # create_user: 是django提供的方法,会对密码进行加密后再保存到数据库
    try:
        print('='*50)
        User.objects.create_user(username=username,
                                 password=pwd,
                                 email=email)
    except Exception as e:
        return render(request, 'register.html', {'message':'用户名已存在'})

    return render(request, 'login.html')