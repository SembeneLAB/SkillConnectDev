# Generated by Django 4.1.7 on 2023-03-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_rename_ob_type_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
