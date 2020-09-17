# Generated by Django 2.2.2 on 2020-04-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0004_auto_20200425_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyTemplateCanisInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('apply_canis_template', models.CharField(max_length=30, verbose_name='应用canis接口模板名称')),
                ('apply_canis_device', models.CharField(max_length=30, verbose_name='应用canis接口设备名称')),
                ('apply_canis_ip', models.CharField(max_length=30, verbose_name='应用canis接口IP地址')),
                ('apply_canis_port', models.CharField(max_length=30, verbose_name='应用canis接口端口号')),
                ('apply_canis_userName', models.CharField(max_length=30, verbose_name='应用canis接口连接用户名')),
                ('apply_canis_pwd', models.CharField(max_length=30, verbose_name='应用canis接口连接密码')),
                ('apply_canis_mode', models.CharField(max_length=30, verbose_name='应用canis接口采集模式')),
                ('apply_canis_bufferSize', models.CharField(max_length=30, verbose_name='应用canis接口缓存区大小')),
                ('apply_canis_sampleRate', models.CharField(max_length=30, verbose_name='应用canis接口采集频率')),
                ('apply_canis_trigger', models.CharField(max_length=30, verbose_name='应用canis接口触发模式')),
                ('apply_canis_drive', models.CharField(max_length=30, verbose_name='应用Canis接口绑定的驱动名称')),
                ('apply_canis_active', models.BooleanField(default=True, verbose_name='应用canis接口是否启动')),
            ],
            options={
                'verbose_name': '应用canis设备模板库记录',
                'db_table': 'gateway_apply_template_canis_interface',
                'verbose_name_plural': '应用canis设备模板库记录',
            },
        ),
        migrations.AlterField(
            model_name='equipmenttemplatecanis',
            name='etc_pip_no',
            field=models.SmallIntegerField(choices=[(0, '通道1'), (1, '通道2'), (2, '通道3'), (3, '通道4'), (4, '通道5'), (5, '通道6')], default=0, verbose_name='Canis通道'),
        ),
    ]