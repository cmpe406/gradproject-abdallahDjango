# Generated by Django 4.1.2 on 2022-11-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_notification_student_notification_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notif_subject',
            field=models.CharField(max_length=200, null=True, verbose_name='Notification subject'),
        ),
    ]