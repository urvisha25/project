# Generated by Django 2.2.4 on 2019-11-25 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmCorner', '0016_auto_20191122_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='eholder',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='farmerreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='startdate',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='talukas',
            name='D_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='traderreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='uploadprice',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
        migrations.AlterField(
            model_name='uproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 21, 17, 40, 511423)),
        ),
    ]
