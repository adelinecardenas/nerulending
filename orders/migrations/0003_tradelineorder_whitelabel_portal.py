# Generated by Django 3.1.1 on 2020-09-04 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0019_subdomain_admins'),
        ('orders', '0002_auto_20200829_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelineorder',
            name='whitelabel_portal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic.subdomain'),
        ),
    ]
