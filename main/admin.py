from django.contrib import admin
from . import models

admin.site.register(models.Chairman)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.StudentAssignment)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','notif_subject','notif_for','notif_read_status']
admin.site.register(models.Notification)

admin.site.register(models.Exam)
admin.site.register(models.ExamQuestions)
admin.site.register(models.CourseExam)
admin.site.register(models.AttemptExam)


