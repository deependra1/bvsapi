# Generated by Django 4.0 on 2024-02-06 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_question', '0002_alter_question_questionnaire'),
        ('bvs_reintegration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reintegration',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bvs_question.question'),
        ),
    ]