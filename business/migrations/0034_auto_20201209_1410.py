# Generated by Django 3.1.1 on 2020-12-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0033_auto_20201209_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tier1',
            old_name='reports_to',
            new_name='company_reports_to',
        ),
        migrations.RenameField(
            model_name='tier2',
            old_name='reports_to',
            new_name='company_reports_to',
        ),
        migrations.RenameField(
            model_name='tier3',
            old_name='reports_to',
            new_name='company_reports_to',
        ),
        migrations.RenameField(
            model_name='tier4',
            old_name='reports_to',
            new_name='company_reports_to',
        ),
    ]