# Generated by Django 4.0 on 2023-09-08 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_ethnic', '0001_initial'),
        ('bvs_religion', '0001_initial'),
        ('bvs_occupation', '0001_initial'),
        ('bvs_burntype', '0001_initial'),
        ('bvs_burncause', '0001_initial'),
        ('bvs_family', '0001_initial'),
        ('bvs_patient', '0008_rename_cause_of_burn_patient_burn_cause_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='burn_cause',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_burncause.burncause'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='burn_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_burntype.burntype'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='degree_of_burn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ethnic_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_ethnic.ethnic'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_family.family'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='material_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='parents_occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents_occupation', to='bvs_occupation.occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_occupation', to='bvs_occupation.occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='percentage_of_burn',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_religion.religion'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='suppose_occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppose_occupation', to='bvs_occupation.occupation'),
        ),
    ]
