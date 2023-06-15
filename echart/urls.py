from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category_sale/',views.category_sale,name='category_sale'),
    path('year_data/',views.year_sales),
    path('segment_data/',views.segment_data),
    path('customer_data/',views.customer_data),
    path('ship/',views.ship),
    path('hot_good/',views.hot_good),
    path('region/',views.region),
    path('price_area/',views.pricearea),



path('load_segment/',views.load_segment_data),
    path('load_category_sale/',views.load_category_sale_data),
    path('loadParetoData/',views.loadParetoData),
    path('visualization01/',views.visualization01),
]
