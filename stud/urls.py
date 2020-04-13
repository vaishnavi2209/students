from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from .views import *


urlpatterns = [

    path('',Home, name='home'),

    #path('aboutus',AboutUs,name='about'),

    path('batches/', BatchesList.as_view() , name='batches'),
    path('batches/details/<int:batchcode>', BatchesDetail, name='batches_detail'),
    path('batches/create', AddBatches.as_view(), name='add_batches'),
    path('batches/<int:pk>/update', UpdateBatchesDetail.as_view() , name='update_batches_detail'),
    path('batches/<int:pk>/delete', DeleteBatchesDetail.as_view() , name='delete_batches_detail'),

    path('courses/', CoursesList.as_view() , name='courses'),
    path('courses/details/<int:ccode>', CoursesDetail, name='courses_detail'),
    path('courses/courseslist',CoursesListPdf),
    path('courses/create', AddCourses.as_view(), name='add_courses'),
    path('courses/<int:pk>/update', UpdateCoursesDetail.as_view() , name='update_courses_detail'),
    path('courses/<int:pk>/delete', DeleteCoursesDetail.as_view() , name='delete_courses_detail'),

    path('students/', StudentsList.as_view() , name='students'),
    path('students/details/<int:admno>',StudentsDetail, name='students_detail'),
    path('students/create', AddStudents.as_view(), name='add_students'),
    path('students/<int:pk>/update', UpdateStudentsDetail.as_view() , name='update_students_detail'),
    path('students/<int:pk>/delete', DeleteStudentsDetail.as_view() , name='delete_students_detail'),

    path('payments/', PaymentsList.as_view() , name='payments'),
    path('payments/details/<int:rpctno>',PaymentsDetail, name='payments_detail'),
    path('payments/create', AddPayments.as_view(), name='add_payments'),
    path('payments/<int:pk>/update', UpdatePaymentsDetail.as_view() , name='update_payments_detail'),
    path('payments/<int:pk>/delete', DeletePaymentsDetail.as_view() , name='delete_payments_detail'),

]

