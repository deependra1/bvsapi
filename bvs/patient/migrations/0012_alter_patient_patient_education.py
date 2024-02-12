# Generated by Django 4.0 on 2024-02-05 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_educationlevel', '0001_initial'),
        ('bvs_patient', '0011_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_educationlevel.educationlevel'),
        ),
    ]
