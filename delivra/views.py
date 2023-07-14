import datetime

from django.contrib.auth.models import User
from django.db.models import Sum
from django.http.response import JsonResponse


def index(request):
    users = User.objects.filter(order__date__lte=datetime.datetime.today(),
                                order__date__gte=datetime.datetime.today() - datetime.timedelta(days=28)).\
        annotate(total_cost=Sum("order__cost"))
    result = users.values("total_cost", "username")
    return JsonResponse(data=list(result), safe=False)
