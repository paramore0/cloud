from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from android_rest.models import User, Product, List
from android_rest.serializers import UserSerializer, ProductSerializer, SearchSerializer


def lists(request):
    if request.method == 'GET':
        datalist = User.objects.all()
        serializer = UserSerializer(datalist, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def loginandroid(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        id = data["id"]
        print(id)
        obj = User.objects.get(id=id)
        print("------------------------=====")
        print(obj)
        if data["password"] == obj.password:
            return JsonResponse("ok", safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse("fail", safe=False, json_dumps_params={'ensure_ascii': False})


def goodsAndorid(request):
    if request.method == 'GET':
        datalist = Product.objects.all()
        serializer = ProductSerializer(datalist, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def searchProduct(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        productName = data["name"]
        productName = productName.replace(" ", "")
        print(productName)
        objs = Product.objects.filter(name__icontains=productName).values('name', 'main', 'nutrition', 'price')
        serializer = SearchSerializer(objs, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii':False})


def searchProductCount(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        productName = data["name"]
        productName = productName.replace(" ", "")
        print(productName)
        objs = Product.objects.filter(name__icontains=productName).values('name')
        objscount = objs.count()
        print(objscount)
        return JsonResponse(objscount, safe=False, json_dumps_params={'ensure_ascii': False})


def infoproduct(request):
    if request.method == 'GET':
        datalist = Product.objects.distinct().all()
        serializer = ProductSerializer(datalist, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def writeList(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        android_id = data["sessionid"]
        productName = data["name"]
        productName = productName.replace(" ", "")
        android_id = android_id.replace(",","")
        print(productName)
        print(android_id)
        objs = Product.objects.filter(name__icontains=productName).values('pno')
        obj = User.objects.filter(id=android_id).values('uno')
        List(uno=obj, pno=objs).save()

