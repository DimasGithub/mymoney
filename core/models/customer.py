from django.db import models
from core.models.helper.base import TimeStampedModel

class Customer(TimeStampedModel, models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True, unique=True)
    password = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True, unique=True)
    avatar = models.ImageField(upload_to='uploads/avatars/%Y/%m/%d',
                               null=True, blank=True, max_length=1000)
    
    class Meta:
        db_table = 'customer'
        ordering = ['-created_at', '-customer_id']
        permissions = (
            ('create-customer', 'can create customer'),
            ('read-customer', 'can read customer'),
            ('update-customer', 'can update customer'),
            ('update-sales-tag-customer', 'can update sales tag customer'),
            ('delete-customer', 'can delete customer')
        )
