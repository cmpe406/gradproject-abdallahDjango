
from django.urls import path
from . import views


urlpatterns = [
     # chairman
     path('chairman/', views.ChairmanList.as_view()),
     path('chairman/<int:pk>/', views.ChairmanDetail.as_view()),
     path('chairman/dashboard/<int:pk>/', views.ChairmanDashboard.as_view()),
     path('chair-login', views.chairman_login),
     path('chairman/change-password/<int:chairman_id>',
          views.chairman_change_password),



     # teacher
     path('', views.CourseList.as_view()),

     path('teacher/', views.TeacherList.as_view()),
     path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
     path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),
     path('teacher-login', views.teacher_login),
     path('teacher/change-password/<int:teacher_id>',
          views.teacher_change_password),

     path('teacher-forgot-password/', views.teacher_forgot_password),
     path('teacher-change-password/<int:teacher_id>/',
          views.teacher_change_password),

     path('verify-teacher/<int:teacher_id>/', views.verify_teacher_via_otp),

     # category
     path('category/', views.CategoryList.as_view()),

     # course
     path('course/', views.CourseList.as_view()),
     path('search-courses/<str:searchstring>', views.CourseList.as_view()),

     # course
     path('course/<int:pk>/', views.CourseDetailView.as_view()),

     # teacher courses
     path('teacher-courses/<int:teacher_id>',
          views.TeacherCourseList.as_view()),
     # teacher course detail
     path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),


     # student
     path('student/', views.StudentList.as_view()),
     path('verify-student/<int:student_id>/', views.verify_student_via_otp),
     path('student-login', views.student_login),
     path('student/<int:pk>/', views.StudentDetail.as_view()),
     path('student/dashboard/<int:pk>/', views.StudentDashboard.as_view()),
     path('student/change-password/<int:student_id>/',
          views.student_change_password),

     path('student-enroll-course/', views.StudentEnrollCourseList.as_view()),
     path('fetch-enroll-status/<int:student_id>/<int:course_id>',
          views.fetch_enroll_status),
     path('fetch-enrolled-students/<int:course_id>',
          views.EnrolledStudentList.as_view()),
     path('fetch-all-enrolled-students/<int:teacher_id>',
          views.EnrolledStudentList.as_view()),
     path('fetch-enrolled-courses/<int:student_id>',
          views.EnrolledStudentList.as_view()),
     path('student-assignment/<int:teacher_id>/<int:student_id>',
          views.AssignmentList.as_view()),
     path('my-assignments/<int:student_id>', views.MyAssignmentList.as_view()),
     path('update-assignments/<int:pk>', views.UpdateAssignments.as_view()),
     path('student/fetch-all-notifications/<int:student_id>/',
          views.NotificationList.as_view()),
     path('save-notification/', views.NotificationList.as_view()),


     #
     path('user-forgot-password/', views.user_forgot_password),
     path('user-change-password/<int:student_id>/', views.user_change_password),

     # Exam
     path('exam/', views.ExamList.as_view()),
     path('add-exam/', views.AddExam.as_view()),

     # specific teacher exam
     path('teacher-exam/<int:teacher_id>', views.TeacherExamList.as_view()),

     # teacher exam detail
     path('teacher-exam-detail/<int:pk>', views.TeacherExamDetail.as_view()),

     # specific exam
     path('exam/<int:pk>', views.ExamDetailView.as_view()),

     path('exam-questions/<int:exam_id>', views.ExamQuestionList.as_view()),
     path('exam-questions/<int:exam_id>/<int:limit>',
          views.ExamQuestionList.as_view()),

     path('add-exam-question/<int:exam_id>', views.ExamQuestionList.as_view()),

     path('fetch-exam-assign-status/<int:exam_id>/<int:course_id>',
          views.fetch_exam_assign_status),
     path('exam-assign-course/', views.CourseExamList.as_view()),
     path('fetch-assigned-exam/<int:course_id>', views.CourseExamList.as_view()),
     path('attempt-exam/', views.AttemptExamList.as_view()),
     path('exam-questions/<int:exam_id>/next-question/<int:question_id>',
          views.ExamQuestionList.as_view()),
     path('fetch-exam-attempt-status/<int:exam_id>/<int:student_id>',
          views.fetch_exam_attempt_status),
     path('attempted-exam/<int:exam_id>', views.AttemptExamList.as_view()),
     path('fetch-exam-result/<int:exam_id>/<int:student_id>',
          views.fetch_exam_result),


     path('send-message/<int:teacher_id>/<int:student_id>',
          views.save_teacher_student_msg),
     path('get-messages/<int:teacher_id>/<int:student_id>',
          views.MessageList().as_view()),

     path('send-group-message/<int:teacher_id>',
          views.save_teacher_student_group_msg),
     path('send-group-message-from-student/<int:student_id>',
          views.save_teacher_student_group_msg_from_student),

     path('fetch-my-teachers/<int:student_id>', views.MyTeacherList.as_view()),

     path('pages/', views.FlatPagesList.as_view()),
     path('pages/<int:pk>/<str:page_slug>/', views.FlatPagesDetail.as_view()),

]
