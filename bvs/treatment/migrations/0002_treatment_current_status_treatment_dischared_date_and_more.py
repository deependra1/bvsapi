# Generated by Django 4.2.4 on 2023-08-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_treatment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='current_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='dischared_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='doctor_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='expired_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='hospitalized_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='hospital',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
