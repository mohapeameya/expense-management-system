# Generated by Django 3.0.7 on 2021-03-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exprecords', '0005_auto_20210310_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exprecord',
            name='proof',
            field=models.ImageField(upload_to='proofs/'),
        ),
    ]
