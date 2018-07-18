from django.shortcuts import render,HttpResponse,redirect
from utils.code import check_code
from django.contrib import auth

# Create your views here.

def code(request):
    img,random_code = check_code()
    request.session['random_code'] = random_code
    # 在内存中读写bytes
    from io import BytesIO
    stream = BytesIO()
    img.save(stream,'png')
    return HttpResponse(stream.getvalue())

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    code = request.POST.get('code')
    if code.upper() != request.session['random_code'].upper():
        return render(request,'login.html',{'msg':'验证码错误'})

    user = auth.authenticate(username=user,password=pwd)
    if user:
        auth.login(request,user)
        return redirect('/index/')

    return render(request, 'login.html', {'msg': '用户名或密码错误'})
