# Generated by Django 5.1 on 2024-08-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_customerdetails_short_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='seat_number',
            field=models.CharField(default=3, max_length=10),
            preserve_default=False,
        ),
    ]
