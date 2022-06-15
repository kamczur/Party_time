# Generated by Django 4.0.4 on 2022-06-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imprezy', '0019_remove_gift_availability_alter_gift_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gift',
            name='reservation_comment',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='GiftReservation',
        ),
    ]
