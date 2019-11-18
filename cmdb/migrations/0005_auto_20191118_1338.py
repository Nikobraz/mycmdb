# Generated by Django 2.2.7 on 2019-11-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20191118_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='ports',
            field=models.ManyToManyField(blank=True, default=None, related_name='_asset_ports_+', through='cmdb.Port', to='cmdb.Asset'),
        ),
    ]
