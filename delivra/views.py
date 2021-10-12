from django.db.models import Sum, Count
from django.http.response import JsonResponse
from .models import Order


def index(request):
    data = []

    result = Order.objects.extra(select={'day': 'date( created_date )'}).values('day', 'product__name',
                                                                                'product__price').annotate(
        total_count=Sum('quantity'))
    for item in result:
        item['total_price'] = item['product__price'] * item['total_count']
        item.pop('product__price')
        data.append(item)

    return JsonResponse(data=data, safe=False)
