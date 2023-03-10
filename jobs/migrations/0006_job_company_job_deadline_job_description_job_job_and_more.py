# Generated by Django 4.1.7 on 2023-03-05 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_profile_aboutme_profile_country_profile_cv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobs.company'),
        ),
        migrations.AddField(
            model_name='job',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='job',
            name='job',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='language',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='job',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='years_of_experience',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
