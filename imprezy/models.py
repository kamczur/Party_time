from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    profil_name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()


class Party(models.Model):
    party_name = models.CharField(max_length=255)
    party_date = models.DateField(null=True)
    party_time = models.TimeField(null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Gift(models.Model):
    gift_name = models.CharField(max_length=255)
    gift_link = models.URLField(null=True)
    comments = models.TextField(null=True)
    party = models.ManyToManyField(Party)


class GiftReservation(models.Model):
    gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    availability = models.BooleanField(default=True)


class Guest(models.Model):
    guest_name = models.CharField(max_length=64)
    guest_surname = models.CharField(max_length=64)
    number_of_adults = models.IntegerField(null=True)
    number_of_children = models.IntegerField(null=True)
    comments = models.CharField(null=True, max_length=256)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)



