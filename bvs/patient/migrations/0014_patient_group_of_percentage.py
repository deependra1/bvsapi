# Generated by Django 4.0 on 2024-02-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_patient', '0013_alter_patient_patient_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='group_of_percentage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
