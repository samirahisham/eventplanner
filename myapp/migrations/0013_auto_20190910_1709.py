# Generated by Django 2.2.5 on 2019-09-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20190910_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
