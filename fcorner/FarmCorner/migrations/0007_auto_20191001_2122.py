# Generated by Django 2.2.4 on 2019-10-01 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmCorner', '0006_auto_20190929_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='uproduct',
            name='T_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buyproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='eholder',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='farmerreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='rentequipment',
            name='startdate',
            field=models.DateField(verbose_name=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='traderreg',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 663164)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='uploadequip',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='uploadprice',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
        migrations.AlterField(
            model_name='uproduct',
            name='Quantity',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='uproduct',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 1, 21, 22, 43, 647540)),
        ),
    ]