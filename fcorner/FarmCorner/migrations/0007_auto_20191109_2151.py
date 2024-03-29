# Generated by Django 2.2.4 on 2019-11-09 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmCorner', '0006_auto_20191108_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadprice',
            name='Price',
        ),
        migrations.AlterField(
            model_name='buyproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 264721)),
        ),
        migrations.AlterField(
            model_name='eholder',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='farmerreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='startdate',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='traderreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 264721)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='hp',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='year',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='uploadprice',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
        migrations.AlterField(
            model_name='uproduct',
            name='Grade',
            field=models.CharField(choices=[('A', 'Grade A'), ('B', 'Grade B'), ('C', 'Grade C')], default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='uproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 21, 51, 55, 249099)),
        ),
    ]
