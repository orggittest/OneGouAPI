# 订单详情API
from rest_framework import serializers

from .models import Order_listModel, CartModel, OrderGoods
from UserApp.api import UserSeraLizer

from UserApp.api import AdderssSeraLizer
from .models import Order_listModel


class Order_listSeraLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order_listModel
        fields = ('id', 'start_time', 'order_statud')


class Order_list_1_SeraLier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderGoods
        fields = ('count',)


class CartModelSeralizer(serializers.ModelSerializer):
    user_id = UserSeraLizer()

    class Meta:
        model = CartModel
        fields = ('id',)
