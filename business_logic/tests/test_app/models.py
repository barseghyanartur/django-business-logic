# -*- coding: utf-8 -*-
#


from django.db import models


class TestModel(models.Model):
    value = models.PositiveIntegerField('value', default=0)

    def __str__(self):
        return str(self.value)

