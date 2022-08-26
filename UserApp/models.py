from django.db import models

from common import YGBaseModel
# from CartList.models import order_listModel

# Create your models here.
class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(bool=True)


class UserModel(YGBaseModel):

    name = models.CharField(max_length=20,
                            verbose_name='用户名')
    phone = models.CharField(max_length=11,
                             verbose_name='手机号', unique=True, blank=True)
    image = models.CharField(max_length=200,
                             verbose_name='用户头像', default='photo/photo.jpg')
    sex = models.IntegerField(choices=((0, '男'), (1, '女')),
                            verbose_name='性别')
    bool = models.BooleanField(default=True,
                               verbose_name='状态')

    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_user'
        verbose_name_plural = verbose_name = '用户表'


class CommentsModel(YGBaseModel):
    order_id = models.ForeignKey('CartList.Order_listModel',
                                 verbose_name='订单ID',
                                 on_delete=models.CASCADE,
                                 related_name='good_comment')
    comments = models.TextField(max_length=500,
                                verbose_name='评论内容')
    comment_time = models.CharField(max_length=30,
                                    verbose_name='评论时间')

    def __str__(self):
        return self.comment_time

    class Meta:
        db_table = 't_comments'
        verbose_name_plural = verbose_name = '评论表'


class NavModel(YGBaseModel):
    nav_child_id = models.ForeignKey('Funy.CategoryModel',
                                     verbose_name='分类ID',
                                     on_delete=models.CASCADE,
                                     related_name='nav',
                                     blank=True,
                                     null=True)
    actives_id = models.ForeignKey('Address.ActivesModel',
                                   verbose_name='活动ID',
                                   on_delete=models.CASCADE,
                                   related_name='Navs',
                                   blank=True,
                                   null=True)
    name = models.CharField(max_length=20,
                            verbose_name='名称')
    image = models.CharField(max_length=200,
                             verbose_name='导航图片')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_nav'
        verbose_name_plural = verbose_name = '导航表'