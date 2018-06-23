# Generated by Django 2.0.6 on 2018-06-23 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0009_auto_20180623_0720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report_trees',
            options={},
        ),
        migrations.AddField(
            model_name='report_trees',
            name='yield_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmer.Yield'),
            preserve_default=False,
        ),
    ]
