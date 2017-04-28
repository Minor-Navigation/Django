# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Users(models.Model):
#     name = models.CharField(max_length=200);
class Users(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    def __unicode__(self):
        return self.first_name    
    