# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.core.urlresolvers import reverse


# Model for Client Names
class Clients(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for Feature Requests
class FeatureReq(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    clientpriority=models.IntegerField()
    target_date=models.DateField(default="mm/dd/yyyy")
    choice = (

        ('Billing', 'billing'),

        ('Policies', 'policies'),

        ('Claims', 'claims'),
        ('Reports', 'reports')
    )

    productarea = models.CharField(max_length=15, choices=choice)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app_feature_request:home')




