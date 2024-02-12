# Generated by Django 4.0 on 2024-02-06 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_followUpSummary', '0001_initial'),
        ('bvs_pshychosocial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychosocial',
            name='number_of_counseling',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='changes_after_intervention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='client_complain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='client_history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='detailed_followup_report',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='followed_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='followup_summary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_followUpSummary.followupsummary'),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='intervention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychosocial',
            name='mode_of_followup',
            field=models.TextField(blank=True, null=True),
        ),
    ]
