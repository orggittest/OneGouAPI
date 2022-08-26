from django.contrib import admin

# Register your models here.
from Address.models import AddressModel, DiscountModel


class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'user', 'state')
    fields = ('address', 'user', 'state')


class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'deduction', 'total_maney', 'datatime', 'periode_of_validity')
    fields = ('user_id', 'deduction', 'total_maney', 'datatime', 'periode_of_validity')


admin.site.register(AddressModel, AddressModelAdmin)
admin.site.register(DiscountModel, DiscountModelAdmin)
