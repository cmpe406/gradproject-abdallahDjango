from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.flatpages.models import FlatPage
from django.core.mail import send_mail
from . import models


class ChairmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = ['id', 'full_name', 'email', 'password',
                  'qualification', 'department', 'profile_img']
        # teacher_courses

    def __init__(self, *args, **kwargs):
        super(ChairmanSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class ChairmanDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['total_teacher_courses', 'total_teacher_courses']
     #   total_teacher_exams


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'password',
                  'qualification', 'department', 'profile_img', 'teacher_courses', 'total_teacher_courses']

    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

    def create(self, validate_data):
        email = self.validated_data['email']
        otp_digit = self.validated_data['otp_digit']
        instance = super(TeacherSerializer, self).create(validate_data)
        send_mail(
            'Verify Account',
            'Please verify your account',
            '19700465@emu.edu.tr',
            [email],
            fail_silently=False,
            html_message=f'<p>Your OTP is </p><p>{otp_digit}</p>'
        )
        return instance


class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['total_teacher_courses', 'total_teacher_exams', 'total_teacher_students']
        # total_teacher_exams


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description', 'total_courses']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title',
                  'description', 'featured_img', 'total_enrolled_students']

    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


# class ExamSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Exam
#         fields = ['id', 'teacher', 'title',
#                   'detail', 'add_time']  # 'assign_status',

#     def __init__(self, *args, **kwargs):
#         super(ExamSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         self.Meta.depth = 0
#         if request and request.method == 'GET':
#             self.Meta.depth = 2


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamQuestions
        fields = ['id', 'questions', 'ans1',
                'ans2', 'ans3', 'ans4', 'right_ans']

    # def __init__(self, *args, **kwargs):
    #     super(QuestionSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     self.Meta.depth = 0
    #     if request and request.method == 'GET':
    #         self.Meta.depth = 1

class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True) # this field should match the related name specified in the model connected to this model
    class Meta:
        model = models.Exam
        fields = ("id","name", "description", "number_of_questions", "time", "course", "questions")

class AddExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exam
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email',
                'password', 'username', 'login_via_otp', 'login_via_otp', 'otp_digit', 'profile_img']

    def __init__(self, *args, **kwargs):
        super(StudentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

    def create(self, validate_data):
        email = self.validated_data['email']
        otp_digit = self.validated_data['otp_digit']
        instance = super(StudentSerializer, self).create(validate_data)
        send_mail(
            'Verify Account',
            'Please verify your account',
            '19700465@emu.edu.tr',
            [email],
            fail_silently=False,
            html_message=f'<p>Your OTP is </p><p>{otp_digit}</p>'
        )
        return instance


class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['enrolled_courses',
                'completed_assignments', 'pending_assignments']
    # total_student_exams


class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ['id', 'course', 'student', 'enrolled_time']

    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAssignment
        fields = ['id', 'teacher', 'student', 'title',
                'detail', 'student_status', 'add_time']

    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['teacher', 'student', 'notif_subject', 'notif_for']


class CourseExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseExam
        fields = ['id', 'teacher', 'course', 'exam', 'add_time']

    def __init__(self, *args, **kwargs):
        super(CourseExamSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class AttemptExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttemptExam
        fields = ['id', 'student', 'exam', 'question', 'right_ans', 'add_time']

    def __init__(self, *args, **kwargs):
        super(AttemptExamSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class FlatPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatPage
        fields = ['id', 'title', 'content', 'url']

# class ContactSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=models.Contact
# 		fields=['id','full_name','email','query_txt']


class TeacherStudentChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherStudentChat
        fields = ['id', 'teacher', 'student',
        'msg_from', 'msg_text', 'msg_time']

    def to_representation(self, instance):
        representation = super(TeacherStudentChatSerializer,self).to_representation(instance)
        representation['msg_time'] = instance.msg_time.strftime(
            "%Y-%m-%d %H:%M")
        return representation
