# Generated by Django 2.0.6 on 2018-06-21 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0012_auto_20180621_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='farm_name',
            new_name='name',
        ),
    ]
