# Generated by Django 4.0.4 on 2022-06-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imprezy', '0017_delete_partygift'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='availability',
            field=models.BooleanField(default=False),
        ),
    ]
