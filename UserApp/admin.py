from django.contrib import admin

# Register your models here.
from UserApp.models import UserModel, CommentsModel, NavModel
from .forms import UserForm


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'image', 'sex', 'bool')
    form = UserForm


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'comments', 'comment_time')
    fields = ('order_id', 'comments', 'comment_time')


class NavModelAdmin(admin.ModelAdmin):
    list_display = ('nav_child_id', 'name', 'image', 'actives_id')
    fields = ('nav_child_id', 'name', 'image', 'actives_id')

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(CommentsModel, CommentsAdmin)
admin.site.register(NavModel, NavModelAdmin)
