from django.db import models
from datetime import datetime
from django.utils.module_loading import import_string
from django.contrib.postgres.fields import JSONField


class Provider(models.Model):
    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS, default='active')
    data = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_client(self):
        print('Provider.get_client init oldu')
        path_ = f'provider.clients.{self.name}.Client'
        class_ = import_string(path_)
        return class_(self.data)

    @property
    def get_adapter(self):
        print('Provider.get_adapter init oldu')
        client = self.get_client

        path_ = f'provider.adapters.{self.name}.Adapter'
        class_ = import_string(path_)
        return class_(client)
    
    class Meta:
        db_table = 'provider'

    def __str__(self):
        return self.name