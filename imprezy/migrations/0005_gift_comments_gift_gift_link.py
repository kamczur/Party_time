# Generated by Django 4.0.4 on 2022-06-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imprezy', '0004_guest_comments_guest_number_of_adults_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='comments',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='gift',
            name='gift_link',
            field=models.URLField(null=True),
        ),
    ]
