from django.db import models
from core.models.customer import Customer

class Wallet(models.Model):
    wallet_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    saldo = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'wallet'
        ordering = ['-created_at', '-wallet_id']
        permissions = (
            ('create-wallet', 'can create wallet'),
            ('read-wallet', 'can read wallet'),
            ('update-wallet', 'can update wallet'),
            ('update-sales-tag-wallet', 'can update sales tag wallet'),
            ('delete-wallet', 'can delete wallet')
        )
