# Generated by Django 2.0.6 on 2018-07-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaleInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=64)),
            ],
        ),
    ]
