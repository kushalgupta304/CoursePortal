# Generated by Django 4.1 on 2022-08-18 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_coursetype_rename_c_name_course_c_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_type',
        ),
        migrations.DeleteModel(
            name='CourseType',
        ),
    ]
