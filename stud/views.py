from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stud.models import  Batches,Courses,Students,Payments
from django.urls import reverse_lazy
#from .forms import CoursesForm
from django_xhtml2pdf.utils import generate_pdf


# Create your views here.
def Home(request):
    return render(request, 'home2.html', None)
    ##return HttpResponse("hello world ")
"""
def AboutUs(request):
    return render(request, 'aboutus.html')
"""
    ##return HttpResponse ("welcome to django Application FRAMEWORK")
def CoursesListPdf(request):
    if request.user.is_authenticated:
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='attachment; filename="output.pdf"'
        context={ 'courses':Courses.objects.all() }
        result= generate_pdf('courses_pdf.html',file_object=response,context=context)
        return result
    else:
        return HttpResponse("you need to login!!")

class BatchesList(generic.ListView):
    model = Batches
    queryset = Batches.objects.all()
    context_object_name = 'batches_list'
    template_name = 'students/batches_list.html'

def BatchesDetail(request,batchcode):
    batches = Batches.objects.get(pk=batchcode)
    context = {'batches': batches}
    return render(request, 'students/batches_detail.html', context)

class AddBatches(CreateView):
   model=Batches
   fields = '__all__'
   template_name='students/batches_form.html'
   success_url=reverse_lazy('Batches')

class UpdateBatchesDetail(UpdateView):
    model = Batches
    fields='__all__'
    template_name='students/batches_form.html'
    success_url=reverse_lazy('home')

class DeleteBatchesDetail(DeleteView):
   #model=Students
   fields='__all__'
   template_name='students/batches_confirm_delete.html'
   success_url=reverse_lazy('batches')

class CoursesList(generic.ListView):
    model =Courses
    fields = '__all__'
    context_object_name = 'courses_list'
    template_name = 'students/courses_list.html'
    success_url = reverse_lazy('home')

def CoursesDetail(request,ccode):
    courses=Courses.objects.get(pk=ccode)
    context={'courses':courses}
    return render(request, 'students/courses_detail.html', context)

class AddCourses(CreateView):
    model = Courses
    fields = '__all__'
    template_name = 'students/courses_form.html'
    success_url = reverse_lazy('home')

class UpdateCoursesDetail(UpdateView):
    model=Courses
    fields='__all__'
    template_name='students/courses_form.html'
    success_url=reverse_lazy('home')

class DeleteCoursesDetail(DeleteView):
    # model = Courses
    fields = '__all__'
    template_name = 'students/courses_confirm_delete.html'  # here students will come bcoz html files are saved in stdents folder
    success_url = reverse_lazy('courses')

class StudentsList(generic.ListView):
    model =Students
    queryset = Students.objects.all()
    context_object_name = 'students_list'
    template_name = 'students/students_list.html'

def StudentsDetail(request,admno):
    students = Students.objects.get(pk=admno)
    context = {'students': students
               }
    return render(request, 'students/students_detail.html', context)

class AddStudents(CreateView):
   model=Students
   fields = '__all__'
   template_name='students/students_form.html'
   success_url=reverse_lazy('students')

class UpdateStudentsDetail(UpdateView):
    model=Students
    fields='__all__'
    template_name='students/students_form.html'
    success_url=reverse_lazy('home')

class DeleteStudentsDetail(DeleteView):
   #model=Students
   fields='__all__'
   template_name='students/students_confirm_delete.html'
   success_url=reverse_lazy('students')

class PaymentsList(generic.ListView):
    model =Payments
    queryset = Payments.objects.all()
    context_object_name = 'payments_list'
    template_name = 'payments/payments_list.html'

def PaymentsDetail(request, rpctno):
    payments = Payments.objects.get(pk=rpctno)
    context = {'payments': payments}
    return render(request, 'payments/payments_detail.html', context)

class AddPayments(CreateView):
   model=Payments
   fields = '__all__'
   template_name='payments/payments_form.html'
   success_url=reverse_lazy('payments')

class UpdatePaymentsDetail(UpdateView):
    model=Payments
    fields='__all__'
    template_name='payments/payments_form.html'
    success_url=reverse_lazy('home')

class DeletePaymentsDetail(DeleteView):
   #model=Students
   fields='__all__'
   template_name='payments/payments_confirm_delete.html'
   success_url=reverse_lazy('payments')

""" Create your views here."""
