# Generated by Django 2.2.7 on 2020-01-30 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_order_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='source_code',
            new_name='final_design',
        ),
    ]
