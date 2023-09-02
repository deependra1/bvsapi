# Generated by Django 4.2.4 on 2023-08-22 10:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('registration_date', models.DateField(auto_now=True)),
                ('fiscal_year', models.CharField(blank=True, max_length=10)),
                ('registration_location', models.CharField(default='KTM', max_length=5)),
                ('registration_number', models.CharField(blank=True, max_length=20, unique=True)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=50, null=True)),
                ('provence', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('local', models.CharField(max_length=50, null=True)),
                ('ward', models.IntegerField(null=True)),
                ('tole', models.CharField(max_length=50, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('age_at_incident', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('citizenship_no', models.CharField(max_length=20, null=True)),
                ('patient_contact', models.CharField(max_length=15, null=True)),
                ('parents_contact', models.CharField(max_length=15, null=True)),
                ('patient_occupation', models.CharField(max_length=50, null=True)),
                ('suppose_occupation', models.CharField(max_length=50, null=True)),
                ('parents_occupation', models.CharField(max_length=50, null=True)),
                ('ethnic_group', models.CharField(max_length=50, null=True)),
                ('religion', models.CharField(max_length=50, null=True)),
                ('family_type', models.CharField(max_length=50, null=True)),
                ('material_status', models.CharField(max_length=50, null=True)),
                ('number_of_child', models.IntegerField(null=True)),
                ('number_of_siblings', models.IntegerField(null=True)),
                ('date_of_incident', models.DateTimeField(null=True)),
                ('area_of_burn', models.CharField(max_length=50, null=True)),
                ('percentage_of_burn', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('degree_of_burn', models.CharField(max_length=50, null=True)),
                ('cause_of_burn', models.CharField(max_length=50, null=True)),
                ('type_of_burn', models.CharField(max_length=50, null=True)),
                ('place_of_incident', models.CharField(max_length=50, null=True)),
                ('description_of_incident', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
