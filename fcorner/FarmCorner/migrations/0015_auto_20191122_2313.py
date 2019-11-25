# Generated by Django 2.2.4 on 2019-11-22 17:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarmCorner', '0014_auto_20191122_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='talukas',
            name='D_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FarmCorner.districts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='eholder',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='farmerreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='startdate',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='traderreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='uploadprice',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
        migrations.AlterField(
            model_name='uproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 13, 28, 511624)),
        ),
    ]