from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import json
from mall import models

STATUS = {'status':False,'name':''}


def login(request):
    ret = {'status': False, 'message': ''}
    if request.method == 'POST':
        user_name = request.POST.get('user_name',None)
        user_pwd = request.POST.get('user_pwd',None)
        obj = models.UserInfo.objects.filter(user=user_name)
        if obj:
            if user_name == obj[0].user and user_pwd == obj[0].passwd:
                ret['status'] = True
                STATUS['status'] = True
                STATUS['name'] = obj[0].user
                return HttpResponse(json.dumps(ret))
            else:
                ret['message'] = '用户名密码错误'
                return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = '用户不存在'
            return HttpResponse(json.dumps(ret))
    return render(request, 'login.html')


def register(request):
    ret = {'status': False, 'message': ''}
    if request.method == 'POST':
        user_name = request.POST.get('user_name',None)
        user_pwd = request.POST.get('user_pwd',None)
        print(user_name,user_pwd)
        print(models.UserInfo.objects.filter(user=user_name).count())
        if models.UserInfo.objects.filter(user=user_name).count() == 0:
            models.UserInfo.objects.create(user=user_name, passwd=user_pwd)
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = "您创建的账号已存在"
            return HttpResponse(json.dumps(ret))
    return render(request, 'register.html')


def home(request):
    ret = {'status':False,'message':''}
    class_list = []
    add_list = []
    cart_num_all = 0
    if request.method == 'POST':
        return_login = request.POST.get('return_login',None)
        if not return_login:
            user_name = request.POST.get('user_name',None)
            money = request.POST.get('money',None)
            num = request.POST.get('num',None)
            p_name = request.POST.get('p_name',None)
            if models.shopping_cart.objects.filter(product_name=p_name).count() == 0:
                models.shopping_cart.objects.create(user_name=user_name, money=money,nember=num,product_name=p_name)
                ret['status'] = True
                return HttpResponse(json.dumps(ret))
            else:
                n_num = models.shopping_cart.objects.filter(product_name=p_name).values('nember')
                now_num = int(n_num[0]['nember'])+int(num)
                models.shopping_cart.objects.filter(product_name=p_name).update(nember=now_num)
                ret['status'] = True
                return HttpResponse(json.dumps(ret))
        else:
            STATUS['status'] = False
            STATUS['name'] = ''
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
    else:
        if STATUS['status']:
            p_obj = models.shopping_cart.objects.filter(user_name=STATUS['name'])
            if p_obj.count() == 0:
                cart_num_all = 0
            else:
                for item in p_obj:
                    cart_num_all = cart_num_all + int(item.nember)
            obj = models.product.objects.all()
            p_num = obj.count()
            tuple_num = divmod(obj.count(),8)
            if tuple_num[1] != 0:
                all_num = tuple_num[0] + 1
            else:
                all_num = tuple_num[0]

            for i in range(1,all_num+1):
                for x in range(8):
                    class_list.append('fy_'+str(i))
            obj = zip(obj,class_list)
            if not request.POST.get('num_id',None):
                return render(request, 'home.html',{'data':list(obj),'num':all_num,'all_num':p_num,
                                                    'user_name':STATUS['name'],'cart_num_all':cart_num_all})
        else:
            return render(request,'login.html')


def cart(request):
    ret = {'status': False,'message':''}
    cart_num_all = 0
    if request.method == "POST":
        p_name = request.POST.get('p_name', None)
        for i in p_name.split('__'):
            models.shopping_cart.objects.filter(product_name=i,user_name=STATUS['name']).delete()
            print(i)
        ret['status'] = True
        return HttpResponse(json.dumps(ret))
    else:
        if STATUS['status']:
            p_obj = models.shopping_cart.objects.filter(user_name=STATUS['name'])
            if p_obj.count() == 0:
                cart_num_all = 0
            else:
                for item in p_obj:
                    cart_num_all = cart_num_all + int(item.nember)
            return render(request, 'cart.html', {'data': p_obj,'user_name': STATUS['name'], 'cart_num_all': cart_num_all})

    return render(request,'login.html')