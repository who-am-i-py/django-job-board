# Generated by Django 4.2.6 on 2023-10-30 05:03

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='pic',
            field=models.ImageField(blank=True, upload_to=job.models.file_upload),
        ),
    ]
