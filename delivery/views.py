
from django.shortcuts import render
from order.models import Shop, Menu, Order, Orderfood

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def delivery(request):
    if request.method == 'GET':
        order_list = Order.objects.all
        return render(request, 'delivery/order_list.html', { 'order_list' : order_list})
    
    elif request.method == 'POST':
        delivery = Order.objects.get(pk = int(request.POST['order_id']))
        delivery.deliver_finish = 1
        delivery.save()
        return render(request, 'delivery/success.html')