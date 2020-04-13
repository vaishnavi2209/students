# Generated by Django 2.2.2 on 2019-07-04 07:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('batchcode', models.IntegerField(help_text='Enter Batch Code', primary_key=True, serialize=False)),
                ('stdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('timings', models.CharField(help_text='Enter Timings', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('ccode', models.IntegerField(help_text='Enter Course Code', primary_key=True, serialize=False)),
                ('cname', models.CharField(help_text='Enter Course Name', max_length=20)),
                ('coursefee', models.IntegerField(help_text='Enter Course Fees')),
                ('duration', models.CharField(max_length=4)),
                ('prereq', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('admno', models.IntegerField(default=uuid.uuid4, help_text='Unique Student ID', primary_key=True, serialize=False)),
                ('rollno', models.IntegerField(help_text='Enter Roll Number')),
                ('fullname', models.CharField(help_text='Enter Full Name', max_length=50)),
                ('fathername', models.CharField(help_text='Enter Fathers Name', max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(help_text='Enter Contact no', max_length=12)),
                ('dj', models.DateField(blank=True, null=True)),
                ('batchcode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stud.Batches')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rpctno', models.IntegerField(help_text='Enter Receipt Number')),
                ('amount', models.IntegerField(help_text='Enter Amount')),
                ('paydate', models.DateField()),
                ('remarks', models.CharField(help_text='Enter Remarks', max_length=200)),
                ('amdno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stud.Students')),
            ],
        ),
        migrations.AddField(
            model_name='batches',
            name='ccode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stud.Courses'),
        ),
    ]
