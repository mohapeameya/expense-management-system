# Generated by Django 3.0.7 on 2021-03-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exprecords', '0003_auto_20210310_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='exprecord',
            name='proof',
            field=models.FileField(default='default.jpg', upload_to='proofs/'),
        ),
    ]
