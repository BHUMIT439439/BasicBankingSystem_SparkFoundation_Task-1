# Generated by Django 3.1.5 on 2021-05-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
            ],
        ),
    ]
