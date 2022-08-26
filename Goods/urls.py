# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

app_name = 'goods_app'

urlpatterns = [
    path('gethome/', GetHomeDataView.as_view(), name='get_home'),
    path('getcate/', GetCateGoodDataView.as_view(), name='get_cate'),
    path('getinfo/', GetGoodInfoView.as_view(), name='get_info')
]
