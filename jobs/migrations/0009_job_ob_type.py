# Generated by Django 4.1.7 on 2023-03-05 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_delete_review_company_description_company_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='ob_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
