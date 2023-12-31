# Generated by Django 4.2.4 on 2023-08-29 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_ethnic', '0001_initial'),
        ('bvs_religion', '0001_initial'),
        ('bvs_occupation', '0001_initial'),
        ('bvs_family', '0001_initial'),
        ('bvs_patient', '0003_alter_patient_parents_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ethnic_group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_ethnic.ethnic'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_family.family'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='parents_occupation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents_occupation', to='bvs_occupation.occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_occupation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_occupation', to='bvs_occupation.occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='religion',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_religion.religion'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='suppose_occupation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppose_occupation', to='bvs_occupation.occupation'),
        ),
    ]
