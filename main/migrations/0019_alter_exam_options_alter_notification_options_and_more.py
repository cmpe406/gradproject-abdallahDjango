# Generated by Django 4.1.2 on 2022-11-12 11:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_notification_notif_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name_plural': '9. Exam'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': '8. Notification'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '5. Student'},
        ),
        migrations.AlterModelOptions(
            name='studentassignment',
            options={'verbose_name_plural': '7. Student Assignments'},
        ),
        migrations.AlterModelOptions(
            name='studentcourseenrollment',
            options={'verbose_name_plural': '6. Enrolled Courses'},
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='description',
            new_name='detail',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='course',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='featured_img',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='remarks',
        ),
        migrations.AddField(
            model_name='exam',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='ExamQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=200)),
                ('ans1', models.CharField(max_length=200)),
                ('ans2', models.CharField(max_length=200)),
                ('ans3', models.CharField(max_length=200)),
                ('ans4', models.CharField(max_length=200)),
                ('right_ans', models.CharField(max_length=200)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.exam')),
            ],
            options={
                'verbose_name_plural': '10. Exam questions',
            },
        ),
        migrations.CreateModel(
            name='CourseExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.exam')),
            ],
            options={
                'verbose_name_plural': '11. Course exam',
            },
        ),
    ]
