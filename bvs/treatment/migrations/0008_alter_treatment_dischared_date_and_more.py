# Generated by Django 4.0 on 2024-02-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_treatment', '0007_alter_treatment_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='dischared_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='expired_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='hospitalized_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
