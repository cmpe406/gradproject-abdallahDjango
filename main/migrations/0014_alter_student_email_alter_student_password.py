# Generated by Django 4.1.2 on 2022-11-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_studentassignment_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]