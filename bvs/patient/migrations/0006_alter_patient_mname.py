# Generated by Django 4.0 on 2023-09-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_patient', '0005_alter_patient_ethnic_group_alter_patient_family_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
