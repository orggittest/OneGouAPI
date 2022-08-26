from django.db import models
from common import YGBaseModel


# Create your models here.
class CityModels(YGBaseModel):
    city_name = models.CharField(verbose_name='城市名称', max_length=10)
    city_letter = models.CharField(verbose_name='首字母名称', max_length=10)
    city_hot = models.IntegerField(verbose_name='热度')

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 't_city'
        verbose_name_plural = verbose_name = '城市'


class CityAreaModels(YGBaseModel):
    cityareaname = models.CharField(verbose_name='区域名称',
                                    max_length=50
                                    )
    city_id = models.ForeignKey(CityModels,
                                verbose_name='所属城市',
                                related_name='citys',
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True
                                )

    def __str__(self):
        return self.cityareaname

    class Meta:
        db_table = 't_city_area'
        verbose_name_plural = verbose_name = '区域'
