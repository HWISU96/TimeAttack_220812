# Generated by Django 4.0 on 2022-07-22 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_jobstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpostactivity',
            name='job_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.jobstatus'),
        ),
    ]
