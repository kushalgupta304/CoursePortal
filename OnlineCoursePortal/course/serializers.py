from rest_framework import serializers
from course.models import Course, Enroll

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class EnrollSerializer(serializers.Serializer):
    class Meta:
        model = Enroll
        fields = '__all__'