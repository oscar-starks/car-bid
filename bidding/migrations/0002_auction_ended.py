# Generated by Django 4.2 on 2023-04-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='ended',
            field=models.BooleanField(default=False),
        ),
    ]
