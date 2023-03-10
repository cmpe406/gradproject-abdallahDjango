# Generated by Django 4.1.2 on 2022-11-15 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_courseexam_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseexam',
            options={'verbose_name_plural': '11. Attempted Questions'},
        ),
        migrations.RemoveField(
            model_name='courseexam',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseexam',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='courseexam',
            name='teacher',
        ),
        migrations.AddField(
            model_name='courseexam',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.examquestions'),
        ),
        migrations.AddField(
            model_name='courseexam',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
    ]
