# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class YGBaseModel(models.Model):
    id = models.CharField(max_length=50, primary_key=True, verbose_name='ID')

    class Meta:
        abstract = True


@receiver(pre_save)
def new_uuid(sender, **kwargs):
    if issubclass(sender, YGBaseModel):
        instance = kwargs.get('instance')
        if not instance.id:
            instance.id = uuid.uuid4().hex
