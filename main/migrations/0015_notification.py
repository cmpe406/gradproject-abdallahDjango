# Generated by Django 4.1.2 on 2022-11-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_student_email_alter_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_text', models.TextField()),
                ('notif_for', models.CharField(max_length=200)),
                ('notif_created_time', models.DateTimeField(auto_now_add=True)),
                ('notif_read_status', models.BooleanField(default=False)),
            ],
        ),
    ]
