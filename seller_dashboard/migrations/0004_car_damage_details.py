# Generated by Django 4.2 on 2023-04-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_dashboard', '0003_car_auctioned'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='damage_details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
