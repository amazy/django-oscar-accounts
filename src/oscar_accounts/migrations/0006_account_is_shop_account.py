# Generated by Django 3.0.12 on 2021-02-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar_accounts', '0005_auto_20210219_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_shop_account',
            field=models.BooleanField(default=False, help_text='This account belongs to the shop'),
        ),
    ]
