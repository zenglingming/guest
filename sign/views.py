from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            # 添加cookie： key，value，有效期
            #response.set_cookie('user', username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username})