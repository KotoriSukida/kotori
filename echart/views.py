from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from echart.models import Sale


# Create your views here.

def index(request):
    # 返回主页面
    return render(request, 'echart/index.html')


class SalesAPIVIew(View):
    def get(self, request):
        """
        查询所有数据
        路由：GET /sale
        """
        queryset = Sale.objects.all().filter(order_Date__contains='2016')
        sale_list = []
        for sale in queryset:
            sale_list.append({
                'id': sale.id,
                'area': sale.area,

            })
        return JsonResponse(sale_list, safe=False,json_dumps_params={'ensure_ascii': False},
)
