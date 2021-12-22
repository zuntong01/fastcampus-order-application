
from django.shortcuts import render
from order.models import Shop, Menu, Order, Orderfood

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', { 'order_list' : order_list})

@csrf_exempt
def time_input(request):
    if request.method == "POST":
        order_item = Order.objects.get(pk=int(request.POST['order_id']))
        order_item.estimated_time = int(request.POST['estimated_time'])
        order_item.save()
        shop_id = order_item.shop.id
        return render(request, 'boss/success.html', { 'shop_id' : shop_id})