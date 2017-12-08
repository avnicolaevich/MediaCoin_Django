import datetime
import uuid

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
    referral_link_path = models.CharField(max_length=10, default='')
    count = models.IntegerField(default=1)
    times = models.IntegerField(default=0)

    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)

    def get_id_str(self):
        return '%s' % (self.id)

class GiftPrice(models.Model):
    price = models.IntegerField(default=0)

class GiftCode(models.Model):
    referral = models.ForeignKey('Referral')
    type = models.BooleanField(default=True)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    amount = models.DecimalField(
        max_digits=16,
        decimal_places=8,
        default=Decimal("0.0")
    )
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)

    def get_code(self):
        return '%s' % (self.code)

class GiftRecipient(models.Model):
    gift_code = models.ForeignKey('GiftCode')
    email = models.EmailField()
    name = models.CharField(max_length=70, blank=True, null=True)

class ReferralTrack(models.Model):
    referral = models.ForeignKey('Referral', null=True, related_name="referral")
    tracked_referral = models.ForeignKey('Referral', null=True, related_name="tracked_referral")