# Generated by Django 4.0 on 2024-02-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvs_question', '0002_alter_question_questionnaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionnaire',
            field=models.TextField(blank=True, null=True),
        ),
    ]
