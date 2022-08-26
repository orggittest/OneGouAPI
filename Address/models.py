from django.db import models
from common import YGBaseModel


# Create your models here.


class AddressModel(YGBaseModel):
    address = models.CharField(max_length=100, verbose_name='用户地址')
    state = models.BooleanField(verbose_name='是否默认', default=True)
    user = models.ForeignKey('UserApp.UserModel', on_delete=models.CASCADE, verbose_name='用户',
                                related_name='addresses', null=True, blank=True)

    class Meta:
        db_table = 't_address'
        verbose_name_plural = verbose_name = '用户地址表'

    def __str__(self):
        return self.address


class DiscountModel(YGBaseModel):
    user_id = models.ForeignKey('UserApp.UserModel', on_delete=models.CASCADE, verbose_name='用户',
                                related_name='discount')
    deduction = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='优惠券额度')
    total_maney = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='满减额度')
    datatime = models.CharField(max_length=20, verbose_name='发放时间')
    periode_of_validity = models.CharField(verbose_name='有效时间', max_length=20)

    class Meta:
        db_table = 't_discount'
        verbose_name_plural = verbose_name = '优惠券表'

    def __str__(self):
        return str(self.deduction)


class ActivesModel(YGBaseModel):
    active_name = models.CharField(max_length=100, verbose_name='活动名称')
    active_url = models.CharField(max_length=100, verbose_name='活动跳转链接', null=True, blank=True)
    icon = models.CharField(max_length=100, verbose_name='活动缩略图', null=True, blank=True)

    class Meta:
        db_table = 't_adtives'
        verbose_name_plural = verbose_name = '活动表'

    def __str__(self):
        return self.active_name
