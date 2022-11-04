from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
import re
from .models import User, Savings, Expenses, Goods


goods = Goods.objects.all()
for i in goods:
    if i.goods_savings:
        print(i.goods_savings)


def main(request):
    if request.method == 'GET':
        user = ''
        if request.user.is_authenticated:
            user = User.objects.filter(username=request.user).all()
            return render(request, 'bankapp/main.html', {"user": user})
        else:
            return render(request, 'bankapp/main.html', {'user': user})


def signup(request):
    if request.method == 'GET':
        return render(request, 'bankapp/signup.html', {'back': '/'})
    else:
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            pat = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
            pass1 = re.search(pat, pass1)
            pass2 = re.search(pat, pass2)
            if pass1 and pass2:
                try:
                    user = User.objects.create_user(request.POST['login'], password=pass1.group(), date_joined=datetime.now())
                    user.save()
                    return redirect('loginuser')
                except IntegrityError as err:
                    return render(request, 'bankapp/signup.html', {'error': 'User already exist'})
            else:
                return render(request, 'bankapp/signup.html', {'error': 'password incorrect try again!'})
        else:
            return render(request, 'bankapp/signup.html', {'error': 'Password didn\'t match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'bankapp/login.html', {'back': '/'})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'bankapp/login.html', {'error': 'Username or password didn\'t match'})
        login(request, user)
        return redirect('main')


def logoutuser(request):
    logout(request)
    return redirect('main')


def savings(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        return render(request, 'bankapp/savings.html', {'back': '/', 'goods': goods})
    else:
        sum = int(request.POST['sum'])
        goods = request.POST.getlist('goods')
        goods_db = ''
        for i in goods:
            goods_db = Goods.objects.filter(goods_savings=i).all()
        saving = Savings(sum=sum, good=goods_db.set())
        saving.save()
        print(goods)
        redirect('main')

