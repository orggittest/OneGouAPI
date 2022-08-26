
from rest_framework import serializers

from Funy.models import CategoryModel,YgeatModel



class CategoryModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'





class YgeatModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = YgeatModel
        fields = "__all__"
