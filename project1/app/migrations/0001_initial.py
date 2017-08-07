# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [#變數目的在跟資料庫做溝通
        migrations.CreateModel(#創建table名稱
            name='Category',#table名稱
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),#沒設pk會預設
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('cash', models.IntegerField()),
                ('balance_type', models.CharField(choices=[('收入', '收入'), ('支出', '支出')], max_length=2)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Category')),
            ],
        ),
    ]
