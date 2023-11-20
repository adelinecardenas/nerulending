# Generated by Django 3.1.1 on 2020-12-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0025_auto_20201209_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=500)),
                ('product', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('tradeline_credit_amount', models.CharField(max_length=500)),
                ('reports_to', models.CharField(max_length=500)),
                ('we_can_help', models.BooleanField(default=True, null=True)),
                ('recommended', models.BooleanField(default=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]