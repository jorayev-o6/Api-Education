from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import *
from main.serializer import *


# Create your views here.

@api_view(['GET'])
def get_banner_view(request):
    banner = Banner.objects.last()
    serializer = BannerSerializer(banner, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


# filter [region, degree, faculty]
@api_view(['GET'])
def search_university_faculty_view(request):
    university = University.objects.filter(region__icontains=region, faculty__id__exact=fuculty_id, degree__id__exact=degree_id)
    serializer = UniversitySerializer(university, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_about_view(request):
    about = About.objects.all().order_by('-id')[:4]
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_popular_university(request):
    popular_university = University.objects.all().order_by('-rating')[:6]
    serializer = UniversitySerializer(popular_university, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_popular_faculty_view(request):
    faculty = University.objects.all().order_by('-rating')[:9]
    serializer = UniversitySerializer(faculty, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_about_me_view(request):
    info = AboutMe.objects.all().order_by('-id')[:6]
    serializer = AboutSerializer(info, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def comment_students_view(request):
    queryset = StudentComment.objects.all().order_by('-id')
    serializer = StudentCommentSerializer(queryset, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def create_phone_view(request):
    try:
        number = request.data.get('number')
        contact = PhoneContact.objects.create(number=number)
        serializers = {
            'success': True,
            'comment': ContactPhoneSerializer(contact).data
        }
        status = HTTP_201_CREATED
    except Exception as e:
        serializers = {
            'success': False,
            'error': f"{e}",
        }
        status = HTTP_500_INTERNAL_SERVER_ERROR
    return Response(serializers, status=status)


@api_view(['GET'])
def search_university_view(request):
    university = University.objects.all()
    serializer = UniversitySerializer(university, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def university_details_view(request, pk):
    university = University.objects.get(id=pk)
    serializer = UniversitySerializer(university, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def student_details_view(request, pk):
    student = Student.objects.get(id=pk)
    serializers = StudentSerializer(student, many=False)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_request_join_university_view(request):
    join = SubmitUniversity.objects.all().order_by('-id')
    serializer = SubmitUniversitySerializer(join, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_request_join_details_view(request, pk):
    join = SubmitUniversity.objects.get(id=pk)
    serializer = SubmitUniversitySerializer(join, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def personal_manager(request):
    manager = PersonalMeneger.objects.last()
    serializer = PersonalManagerSerializer(manager, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_count_info_view(request):
    count = Student.objects.all().count()
    print(count)
    serializers = StudentSerializer(count, many=True)
    return Response(serializers.data, status=HTTP_200_OK)



































