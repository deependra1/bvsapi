# Generated by Django 4.0 on 2023-09-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_funding', '0005_alter_funding_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='service_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
