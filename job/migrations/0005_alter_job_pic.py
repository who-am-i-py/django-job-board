# Generated by Django 4.2.6 on 2023-10-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='pic',
            field=models.ImageField(upload_to='job/job_pics'),
        ),
    ]
