from django.db import models
from common import YGBaseModel



# Create your models here.

from common import YGBaseModel


class CategoryModel(YGBaseModel):
    name = models.CharField(max_length=10,verbose_name='分类名')
    category_url = models.CharField(max_length=200,verbose_name='分类图片',null=True,blank=True)
    father_id = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,verbose_name='父分类名')

    def __str__(self):
        return self.name



    class Meta:
        db_table = 't_category'
        verbose_name_plural = verbose_name = '分类表'




class YgeatModel(YGBaseModel):
    eat_img = models.CharField(max_length=200,verbose_name='图片地址')
    eat_content = models.CharField(max_length=50,verbose_name='描述')
    eat_time = models.CharField(max_length=20,verbose_name='时间')
    hot = models.IntegerField(verbose_name='热度')


    class Meta:
        db_table = 't_ygeat'
        verbose_name_plural = verbose_name = '吃喝玩乐'



