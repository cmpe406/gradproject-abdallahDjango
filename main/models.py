from django.db import models


# Chairman
class Chairman(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200)
    department = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='chair_imgs/', null=True)

    class Meta:
        verbose_name_plural = "1. Chairman"


# Teacher
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200)
    department = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='teacher_imgs/', null=True)

    class Meta:
        verbose_name_plural = "2. Teacher"
    
    def __str__(self):
        return f'{self.full_name}'

    def total_teacher_courses(self):
        total_courses = Course.objects.filter(teacher=self).count()
        return total_courses

    def total_teacher_exams(self):
        counter=0
        courses=Course.objects.filter(teacher=self)
        for course in courses:
            for exam in course.course_exams():
                counter+=1
        return counter

    def total_teacher_students(self):
        total_students = StudentCourseEnrollment.objects.filter(
            course__teacher=self).count()
        return total_students
    
    def teacher_exams(self):
        courses=Course.objects.filter(teacher=self)
        exams_lst = []
        for course in courses:
            for exam in course.course_exams():
                exams_lst.append(exam)
        return exams_lst



# Course category model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "3. Course Categories"

    def __str__(self):
        return self.title

    def total_courses(self):
        return Course.objects.filter(category=self).count()

# Student
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=200)
    profile_img = models.ImageField(upload_to='student_imgs/', null=True)
    verify_status = models.BooleanField(default=False)
    otp_digit = models.CharField(max_length=10, null=True)
    login_via_otp = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "5. Student"

    def __str__(self):
        return self.full_name

    def enrolled_courses(self):
        enrolled_courses = StudentCourseEnrollment.objects.filter(
            student=self).count()
        return enrolled_courses

    def completed_assignments(self):
        completed_assignments = StudentAssignment.objects.filter(
            student=self, student_status=True).count()
        if completed_assignments > 0:
            return completed_assignments
        else:
            return 0

    def pending_assignments(self):
        pending_assignments = StudentAssignment.objects.filter(
            student=self, student_status=False).count()
        if pending_assignments > 0:
            return pending_assignments
        else:
            return 0
    # def total_student_exams(self):
    #     total_student_exams = Exam.objects.filter(course__student=self).count()
    #     return total_student_exams



class StudentAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    student_status = models.BooleanField(default=False, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "7. Student Assignments"


# Course model
class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    featured_img = models.ImageField(upload_to='course_imgs/', null=True)
    prerequisites = models.TextField(null=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='category_courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_courses')
    student = models.ManyToManyField(Student, related_name='course_student')


    class Meta:
        verbose_name_plural = "4. Course"

    def __str__(self):
        return self.title

    def total_enrolled_students(self):
        total_enrolled_students = StudentCourseEnrollment.objects.filter(
            course=self).count()
        return total_enrolled_students
    
    # returns all exams related to a certain course
    def course_exams(self):
        return self.examss.all()

# student course enrollment
class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='enrolled_courses')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='enrolled_student')
    enrolled_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.student}"

    class Meta:
        verbose_name_plural = "6. Enrolled Courses"


# exams
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True,related_name="examss")
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    number_of_questions = models.IntegerField(null=True)
    time = models.IntegerField(help_text="duration of the exam(in mins.)", null=True)

    class Meta:
        verbose_name_plural="Exams"

    def __str__(self):
        return f"Exam: {self.name}"
        # return "Exam "+str(self.id)
    
    def get_questions(self):
        return self.questions.all()[:self.number_of_questions]
    
    # def get_absolute_url(self):
    #     return reverse("exams:exam-detail", kwargs={"id": self.id}) # need to specify the app name that we added in urls.py file

# quiz model
# class Exam(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=200)
#     detail = models.TextField()
#     add_time = models.DateTimeField(auto_now_add=True)

#     def assign_status(self):
#         return CourseExam.objects.filter(exam=self).count()

#     class Meta:
#         verbose_name_plural = "9. Exam"


# class Exam(models.Model):
#     course = models.ForeignKey(
#         Course, on_delete=models.CASCADE, related_name='course_exams')
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     featured_img = models.ImageField(upload_to='course_imgs/', null=True)
#     remarks = models.TextField(null=True)
#
#     class Meta:
#         verbose_name_plural = "5. Exams"


# quiz question model

class ExamQuestions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, related_name='questions')
    questions = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    right_ans = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "10. Exam questions"


# notifications model

class Notification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    notif_subject = models.CharField(
        max_length=200, verbose_name='Notification subject', null=True)
    notif_for = models.CharField(
        max_length=200, verbose_name='Notification For')
    notif_created_time = models.DateTimeField(auto_now_add=True)
    notif_read_status = models.BooleanField(
        default=False, verbose_name='Notification Status')

    class Meta:
        verbose_name_plural = "8. Notification"


# add quiz to course

class CourseExam(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "11. Course exam"


# add exam question by student

class AttemptExam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(
        ExamQuestions, on_delete=models.CASCADE, null=True)
    right_ans = models.CharField(max_length=200, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "12. Attempted Questions"


# class Contact(models.Model):
#     	full_name=models.CharField(max_length=100)
# 	email=models.EmailField()
# 	query_txt=models.TextField()
# 	add_time=models.DateTimeField(auto_now_add=True)

# 	def __str__(self) -> str:
# 		return self.query_txt

# 	def save(self,*args, **kwargs):
# 		send_mail(
# 			'Contact Query',
# 			'Here is the message.',
# 			'codeartisanlab2607@gmail.com',
# 			[self.email],
# 			fail_silently=False,
# 			html_message=f'<p>{self.full_name}</p><p>{self.query_txt}</p>'
# 		)
# 		return super(Contact,self).save(*args, **kwargs)

# 	class Meta:
# 		verbose_name_plural="17. Contact Queries"


# Messages
class TeacherStudentChat(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    msg_text = models.TextField()
    msg_from = models.CharField(max_length=100)
    msg_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "18. Teacher Student Messages"
