# 购物车信息
from datetime import datetime

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from CartList.models import OrderGoods
from UserApp.models import UserModel
from .api import Order_list_1_SeraLier, Order_listModel, CartModel
from Goods.api import GoodsModel, GoodsModel_twoSerializers, GoodsInfoModel, GoodsImage_OneSerializers, GoodsImageModel
from Address.models import AddressModel


class GetCartView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        goods = request.POST.get('goods_id')
        users = request.session.get('user')
        print(users)

        order_id = Order_listModel.objects.filter(user_id=users).first()
        count = Order_list_1_SeraLier(instance=order_id).data

        goods_info = GoodsModel.objects.filter(id=users).first()
        goods_data = GoodsModel_twoSerializers(instance=goods_info).data

        return JsonResponse({
            "cart_datas": [
                {
                    "goods_id": goods,
                    "goods_num": count,
                    "user_id": users,
                    "goods_detail": goods_data
                }
            ]
        })


class AddCartView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        goods_id = request.POST.get('goods_id')
        users = request.session.get('user')
        user_id = users['id']
        userse = UserModel.objects.get(id=user_id)
        print(user_id)

        user_cart = CartModel.objects.filter(user_id=user_id).all()
        print(user_cart)
        address_id = AddressModel.objects.filter(Q(user_id=user_id) & Q(state=True)).first()
        print(address_id)
        add = request.POST.get('add_goods')
        sub = request.POST.get('sub_goods')
        if add:
            order_list = OrderGoods.objects.filter(order__user__id=user_id, goods_id=goods_id).first()
            print(order_list)
            print('数量', order_list.count)

            if order_list:
                order_list.count += 1
                order_list.save()
                return JsonResponse({
                    'code': 200,
                    'msg': '商品增加成功'
                })

            else:
                order = Order_listModel.objects.filter(user_id=user_id).first()
                print('Order_______', order)

                start_time = str(datetime.now())
                order_statud = 1
                goods = GoodsModel.objects.get(id=goods_id)
                Order_listModel(user=userse, start_time=start_time, order_statud=order_statud,
                                addr_id=address_id).save()
                OrderGoods(order=order, goods=goods, count=1).save()
                OrderGoods(count=1).save()

        elif sub:
            order_list = OrderGoods.objects.filter(order__user__id=user_id, goods_id=goods_id).first()
            if order_list:
                order_list.count -= 1
                order_list.save()
                return JsonResponse({
                    'code': 200,
                    'msg': '商品减少成功'
                })
        else:
            return JsonResponse({
                'code': 200,
                'msg': '请从操作'
            })


class OrderDownView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # 获取商品的数量
        order_num = request.POST.get('order_num')

        # 获取商品的优惠价以及总价
        goods_id = request.POST.get('goods_id')
        goods = GoodsInfoModel.objects.get(goods_id=goods_id)
        goods_price = goods.sellprice
        price = goods_price * int(order_num)

        # 获取地址
        # 如果用户填写地址以及手机号和姓名等信息
        address = request.POST.get('address', None)
        phone = request.POST.get('phone', None)
        name = request.POST.get('name', None)

        # 获取商品的名字
        goods_name = goods.goods_id.commodityname

        # 获取商品的图片
        goods_img = GoodsImageModel.objects.filter(goods_id=goods_id).all()
        goods_img_serializer = GoodsImage_OneSerializers(instance=goods_img, many=True)

        return JsonResponse({
            "code": 200,
            "order_num": order_num,
            "total_price": price,
            "addr": {
                "phone": phone,
                "name": name,
                "address": address
            },
            "goods": [
                {
                    "img": goods_img_serializer.data,
                    "price": goods_price,
                    "cnt": order_num
                }
            ]
        })


class CartSumView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # 获取当前用户所有的订单
        user = request.session.get('user')
        user_id = user['id']
        order = OrderGoods.objects.filter(order__user__id=user_id).all()
        sum = 0
        for i in order:
            sum += (i.count * i.goods.originalprice)

        return JsonResponse({
            'code': 200,
            'sum':sum,
            'msg':'总价计算成功'
        })
