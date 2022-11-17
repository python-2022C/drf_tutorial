# Generated by Django 4.1.3 on 2022-11-17 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.course'),
        ),
    ]
