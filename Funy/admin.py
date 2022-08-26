from django.contrib import admin

# Register your models here.
from .models import CategoryModel, YgeatModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_url', 'father_id')
    search_fields = ('name', 'father_id')
    fields = ('name', 'category_url', 'father_id')


class YgeatAdmin(admin.ModelAdmin):
    list_display = ('id','eat_img','eat_content','eat_time','hot')
    fields = ('eat_img','eat_content','eat_time','hot')





admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(YgeatModel, YgeatAdmin)
