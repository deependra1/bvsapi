# Generated by Django 4.0 on 2024-02-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
