# Generated by Django 4.0 on 2024-02-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_donor', '0002_alter_donor_donor_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donor_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
