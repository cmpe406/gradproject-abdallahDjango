# Generated by Django 4.1.2 on 2022-11-15 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_attemptexam_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='attemptexam',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.exam'),
        ),
    ]
