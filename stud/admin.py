from django.contrib import admin
#from django.contrib.admin import ModelAdmin
from .models import Courses,Batches,Students,Payments

# Register your models here.
 ## @ will not be used becoz that will form a decorator nd we dont need that.
admin.site.register(Batches)
admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(Payments)


##@admin.site.register(Courses)
class BatchesAdmin():
    list_display=('batchcode', 'ccode')
    fieldsets=(
        ('batches Entry',
         {'fields': ('batchcode', 'ccode', 'stdate')}
         ),
        ('batches details',
         {'fields': (('enddate', 'timings'))}
         )
    )


class CoursesAdmin():
    list_display=('ccode', 'cname')
    fieldsets=(
        ('Courses Entry',
         {'fields': ('ccode', 'cname', 'coursefee')}
         ),
        ('courses details',
         {'fields': (('duration', 'prereq'))}
         )
    )

class Student():

    list_display = ('admno', 'fullname')
    fieldsets = (
        ('Student Entry',
         {'fields': ('batchcode', 'rollno', 'fathername')}
        ),
        ('Student details',
         {'fields': (('email', 'phone', 'dj'))}
         )
    )

class Payments():
    list_display = ('rpctno', 'amdno')
    fieldsets = (
        ('Payments Entry',
         {'fields': ('amount', 'paydate', 'remarks')}
         )
        )

empty_value_list = '--empty--'

