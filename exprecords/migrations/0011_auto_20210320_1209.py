# Generated by Django 3.0.7 on 2021-03-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exprecords', '0010_auto_20210319_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exprecord',
            name='description',
        ),
        migrations.AlterField(
            model_name='exprecord',
            name='item',
            field=models.CharField(max_length=1024),
        ),
    ]