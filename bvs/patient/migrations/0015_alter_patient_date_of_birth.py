# Generated by Django 4.0 on 2024-02-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_patient', '0014_patient_group_of_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]