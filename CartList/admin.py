from django.contrib import admin
from .models import  Order_listModel, CartModel, OrderGoods


# Register your models here.
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'goods', 'count')
    fields = ('user', 'goods', 'count')


class OrderListModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_time', 'order_statud','addr_id')
    fields = ('user', 'start_time', 'order_statud', 'addr_id')

class OrderGoodsAdmin(admin.ModelAdmin):
    list_display = ('order', 'goods', 'count')
    fields = ('order', 'goods', 'count')


admin.site.register(CartModel, CartModelAdmin)
admin.site.register(Order_listModel, OrderListModelAdmin)
admin.site.register(OrderGoods, OrderGoodsAdmin)
