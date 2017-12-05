import datetime

from decimal import Decimal
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class WalletTransaction(models.Model):
#     created_at = models.DateTimeField(default=datetime.datetime.now)
#
#     from_wallet = models.ForeignKey(
#         'Wallet',
#         null=True,
#         related_name="sent_transactions"
#     )
#     to_wallet = models.ForeignKey(
#         'Wallet',
#         null=True,
#         related_name="received_transactions"
#     )
#
#     to_bitcoinaddress = models.CharField(
#         max_length=50,
#         blank=True
#     )
#
#
# class Wallet(models.Model):
#     created_at = models.DateTimeField(default=datetime.datetime.now)
#     updated_at = models.DateTimeField()
#
#     label = models.CharField(max_length=50, blank=True)
#
#     transactions_with = models.ManyToManyField(
#         'self',
#         through=WalletTransaction,
#         symmetrical=False)
#
#     transaction_counter = models.IntegerField(default=1)
#
#     last_balance = models.DecimalField(default=Decimal(0), max_digits=16, decimal_places=8)

class Transaction(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now)
    amount = models.DecimalField(
        max_digits=16,
        decimal_places=8,
        default=Decimal("0.0")
    )
    address = models.CharField(max_length=50)

    referral = models.ForeignKey('Referral')

class Referral(models.Model):
    author = models.ForeignKey('auth.User', blank=True, null=True)
    referral_id = models.CharField(max_length=36)
    web3addr = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)