# Generated by Django 3.1.5 on 2021-05-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customer_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_no',
            field=models.IntegerField(),
        ),
    ]
