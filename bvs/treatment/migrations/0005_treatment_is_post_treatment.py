# Generated by Django 4.0 on 2023-10-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_treatment', '0004_remove_treatment_current_status_treatment_distance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='is_post_treatment',
            field=models.BooleanField(null=True),
        ),
    ]
