# Generated by Django 4.1.2 on 2023-01-07 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='login_via_otp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='TeacherStudentChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_text', models.TextField()),
                ('msg_from', models.CharField(max_length=100)),
                ('msg_time', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'verbose_name_plural': '18. Teacher Student Messages',
            },
        ),
    ]
