import re

from django import forms
from django.core.exceptions import ValidationError

"""
user模型数据的定制化
"""

from .models import UserModel

class UserForm(forms.ModelForm):
    name = forms.CharField( label='昵称',
                           min_length=8,
                           max_length=20,
                           required=True,
                           # 该字段定制
                            error_messages={
                                'required': '昵称不能为空',
                                "min_length": '昵称长度不能小于8位',
                                'max_length': '昵称长度不能大于8位'
                            })
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            required=False)

    class Meta:
        model = ''
        fields = ('name', 'phone', 'image', 'sex', 'bool')

    def is_valid(self):
        return super().is_valid()

    # 自定义手机验证
    def yan_phone(self):
        phone = self.cleaned_data.get('phone')
        if re.search(r'[1]{ 3, 5, 8, 9 }\d+', phone):
           return phone
        raise ValidationError('错误的手机号')