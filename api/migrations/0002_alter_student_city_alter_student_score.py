# Generated by Django 4.1.3 on 2022-11-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, default='Jizzax', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
