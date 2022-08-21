from rest_framework.viewsets import ModelViewSet
from .serializers import CourseSerializer
from .models import Course, Enroll

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class CourseViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class= CourseSerializer
    queryset=Course.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.user_type == 'educator':
            data = request.data 
            data.update({"educator":request.user.id})
            obj = CourseSerializer(data =data)
            if obj.is_valid():
                obj.save()
                return Response({"message":"Course created"})
            else:
                return Response({"message":"unable to create course", "errors": obj.errors}, status = 403)
        else:
            return Response({"message":"unable to create course you are not educator"}, status=403)


class EnrollApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        # need to check if given course exists or not
        course_obj = Course.objects.get(id = request.data['course_id'])
        Enroll.objects.get_or_create(course=course_obj, user= request.user)
        return Response({"message": "success"})

    def get(self, request):
        courses = Enroll.objects.filter(user= request.user).values('course')
        
        return Response({"enrolled_courses":courses})



class CourseAnalytics(APIView):
    def get(self, request):
        courses = Course.objects.filter(educator = request.user)
        analytics = []

        for c in courses:
            count = Enroll.objects.filter(course=c).count()
            analytics.append({"course_name":c.c_name, "enrollments": count})

        
        return Response({"analytics":analytics})
