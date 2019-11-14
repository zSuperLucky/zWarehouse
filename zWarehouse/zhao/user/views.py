from django.shortcuts import render,HttpResponse,redirect
from user import models
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upswd = request.POST.get('upswd')
        user_obj = models.UserInfo.objects.filter(uname=uname, upswd=upswd).first()
        if user_obj:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('用户名或密码错误')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upswd = request.POST.get('upswd')
        re_upswd = request.POST.get('re_upswd')
        if uname and upswd and re_upswd:
            if upswd == re_upswd:
                user_obj = models.UserInfo.objects.filter(uname=uname).first()
                if user_obj:
                    return HttpResponse('用户已存在')
                else:
                    models.UserInfo.objects.create(uname=uname, upswd=upswd).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次密码不一致')
        else:
            return HttpResponse('不能有空！')