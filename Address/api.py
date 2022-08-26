# -*- coding: utf-8 -*-
from .models import ActivesModel

from rest_framework import serializers


class ActiveSerializer(serializers.ModelSerializer):
    class Mata:
        model = ActivesModel
        fields = ['active_name', 'active_url', 'icon']
