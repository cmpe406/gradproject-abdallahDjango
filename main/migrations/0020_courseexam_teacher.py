# Generated by Django 4.1.2 on 2022-11-12 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_exam_options_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseexam',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
    ]