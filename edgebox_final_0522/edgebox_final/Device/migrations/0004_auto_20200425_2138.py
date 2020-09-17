# Generated by Django 2.2.2 on 2020-04-25 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0003_auto_20200425_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmenttemplatecanis',
            name='etc_pip_no',
            field=models.SmallIntegerField(choices=[(1, '通道1'), (2, '通道2'), (3, '通道3'), (4, '通道4'), (5, '通道5'), (6, '通道6')], default=0, verbose_name='Canis通道'),
        ),
    ]