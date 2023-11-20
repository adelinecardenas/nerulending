# Generated by Django 3.1.1 on 2020-09-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0061_auto_20200914_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='business_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Business Name'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='business_street_address_1',
            field=models.CharField(max_length=255, null=True, verbose_name='Business Address Line 1'),
        ),
    ]
