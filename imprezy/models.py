from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

class Party(models.Model):
    party_name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Gift(models.Model):
    gift_name = models.CharField(max_length=255)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

class Guest(models.Model):
    guest_name = models.CharField(max_length=64)
    guest_surname = models.CharField(max_length=64)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)



