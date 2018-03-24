import re

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View

from apps.users.models import User


class RegisterView(View):
    """类视图,处理注册"""

    def get(self, request):
        """处理get请求"""
        # 获取注册页面
        return render(request, 'register.html')

    def post(self, request):
        """处理post请求"""
        # 处理注册逻辑

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
            print('*' * 10)
            return render(request, 'register.html', {'message': '请填满所有参数'})

        # 判断两次输入的密码是否一致
        if pwd != cpwd:
            print('-' * 10)
            return render(request, 'register.html', {'message': '两次输入的密码不一致'})

        # 判断是否勾选了用户协议
        if allow != 'on':
            print('+' * 10)
            return render(request, 'register.html', {'message': '请先同意用户协议'})

        # 判断邮箱格式是否正确
        if not re.match('^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            print('/' * 10)
            return render(request, 'register.html', {'message': '邮箱格式不正确'})

        # 业务处理
        # 保存用户到数据库中
        # create_user: 是django提供的方法,会对密码进行加密后再保存到数据库
        try:
            print('=' * 50)
            User.objects.create_user(username=username,
                                     password=pwd,
                                     email=email)
        except Exception as e:
            return render(request, 'register.html', {'message': '用户名已存在'})

        return redirect(reverse("users:login"))


class LoginView(View):
    """类视图,处理登录"""
    def get(self, request):
        """进入登录界面"""
        return render(request, 'login.html')

    def post(self, request):
        """处理登录逻辑"""
        # 获取登录参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验参数合法性
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg':'请将所有参数填满'})

        # 通过 django 提供的authenticate方法，
        # 验证用户名和密码是否正确
        user = authenticate(username=username, password=password)

        # 用户名或密码不正确
        if user is None:
            return render(request, 'login.html', {'errmsg':'用户名或密码不正确'})

        # 注册账号未激活
        if not user.is_alive:
            return render(request, 'login.html', {'errmsg':'请先激活账号'})

        # 通过django的login方法，保存登录用户状态（使用session）
        login(request, user)

        # 获取是否勾选‘记住用户名’
        remember = request.session.get('remember')

        # 判断是否勾上记住用户名和密码
        if remember != 'on':
            # 没有勾选,不需记住cookie信息,浏览会话结束后过期
            request.session.set_expiry(0)
        else:
            # 已勾选,需要记住cookie信息,两周后过期
            request.session.set_expiry(None)

        # 响应请求，返回html界面 (进入首页)
        return redirect(reverse('goods:index'))


class LogoutView(View):
    """退出登录"""

    def get(self, request):

        # 由django用户认证系统完成，会清理cookie
        # 和session,request参数中有user对象
        logout(request)

        # 推出后跳转，由产品经理设计
        return redirect(reverse('goods:index'))


class ActiveView(View):

    def get(self, request, token):
        # 激活成功进入登录界面
        return redirect(reverse("users:login"))
