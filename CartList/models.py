from django.db import models

# Create your models here.
from django.db import models
from common import YGBaseModel


class CartModel(YGBaseModel):
    user = models.ForeignKey('UserApp.UserModel',
                             on_delete=models.CASCADE,
                             verbose_name='用户ID',
                             related_name='user')
    goods = models.ForeignKey('Goods.GoodsModel',
                              on_delete=models.CASCADE,
                              verbose_name='商品',
                              related_name='cart')
    count = models.IntegerField(verbose_name='数量',
                                default=1)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 't_cart'
        verbose_name_plural = verbose_name = '购物车表'


class Order_listModel(YGBaseModel):
    user = models.ForeignKey('UserApp.UserModel',
                             on_delete=models.CASCADE,
                             verbose_name='所属用户',
                             related_name='order')
    start_time = models.CharField(max_length=50, verbose_name='下单时间')
    order_statud = models.IntegerField(choices=((0, '待支付'),
                                                (1, '已支付'),
                                                (2, '已取消'),
                                                (3, '待发货'),
                                                (4, '已发货'),
                                                (5, '已完成')),
                                       verbose_name='订单状态')
    addr_id = models.ForeignKey('Address.AddressModel', on_delete=models.CASCADE, verbose_name='订单地址',
                                related_name='addrs')

    def __str__(self):
        return self.id

    class Meta:
        db_table = 't_orderlist'
        verbose_name_plural = verbose_name = '订单详情表'


class OrderGoods(YGBaseModel):
    order = models.ForeignKey('Order_listModel',
                              on_delete=models.CASCADE,
                              verbose_name='所属订单',
                              related_name='goods')
    goods = models.ForeignKey('Goods.GoodsModel',
                              on_delete=models.CASCADE,
                              verbose_name='商品',
                              related_name='order')
    count = models.IntegerField(verbose_name='购买数量')

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 't_ordergoods'
        verbose_name_plural = verbose_name = '订单商品详情表'
