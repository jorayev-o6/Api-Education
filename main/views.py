from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import *
from main.serializer import *


# Create your views here

@api_view(['GET'])
def get_banner_view(request):
    banner = Banner.objects.last()
    serializer = BannerSerializer(banner, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


# filter [region, degree, faculty]
@api_view(['GET'])
def search_university_faculty_view(request):
    region = request.GET.get('region')
    faculty_id = request.GET.get('faculty_id')
    degree_id = request.GET.get('degree_id')
    university = University.objects.filter(region__icontains=region, faculty__id__exact=faculty_id, degree__id__exact=degree_id)
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
    search = request.GET.get('university')
    university = University.objects.filter(name__icontains=search)
    serializer = UniversitySerializer(university, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def university_details_view(request, pk):
    university = University.objects.get(id=pk)
    serializer = UniversitySerializer(university, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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
def get_count_info_view(request, pk):
    university = University.objects.get(id=pk)
    students_count = Student.objects.filter(university_id=pk).count()
    registers_count = SubmitUniversity.objects.filter(university_id=pk).count()
    accepted_count = SubmitUniversity.objects.filter(status=2).count()
    cancelled_count = SubmitUniversity.objects.filter(status=3).count()
    students = Student.objects.filter(university_id=pk)
    male_count = students.filter(gender=1).count()
    female_count = students.filter(gender=2).count()

    data = {
        'university': UniversitySerializer(university).data,
        'students': students_count,
        'register': registers_count,
        'accepted': accepted_count,
        'cancelled': cancelled_count,
        'gender': {
            'male': male_count,
            'female': female_count,
        },
    }
    return Response(data, status=HTTP_200_OK)


@api_view(['GET'])
def get_students_view(request, pk):
    students = Student.objects.filter(university_id=pk).order_by('-id')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_university_registered_view(request, pk):
    register = SubmitUniversity.objects.get(student_id=pk)
    register.status = request.GET.get('status')
    register.save()
    if register.status == '1':
        data = {
            'serializer': SubmitUniversitySerializer(register).data,
            'success': True,
            'message': 'You have successfully joined the university',
        }
    elif register.status == '2':
        data = {
            'serializer': SubmitUniversitySerializer(register).data,
            'success': False,
            'message': 'Sorry! You have cancelled the university',
        }
    return Response(data, status=HTTP_200_OK)


@api_view(['GET'])
def students_filter_view(request):
    students = request.GET.get('student')
    student = Student.objects.filter(first_name__icontains=students, last_name__icontains=students)
    serializers = StudentSerializer(student, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_university_single_view(request, pk):
    university = University.objects.get(university_id=pk)
    serializer = UniversitySerializer(university)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def dashboard_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Error username or password please check your password or username'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'}, status=HTTP_401_UNAUTHORIZED)
    return Response({'message': 'Login successful'}, status=HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_dashboard_view(request, pk):
    university = University.objects.get(id=pk)
    students_count = Student.objects.filter(university_id=pk).count()
    registers_count = SubmitUniversity.objects.filter(university_id=pk).count()
    accepted_count = SubmitUniversity.objects.filter(status=2).count()
    cancelled_count = SubmitUniversity.objects.filter(status=3).count()
    students = Student.objects.filter(university_id=pk)
    male_count = students.filter(gender=1).count()
    female_count = students.filter(gender=2).count()

    data = {
        'university': UniversitySerializer(university).data,
        'students': students_count,
        'register': registers_count,
        'accepted': accepted_count,
        'cancelled': cancelled_count,
        'gender': {
            'male': male_count,
            'female': female_count,
        },
    }
    return Response(data, status=HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_universities_view(request):
    universities = University.objects.all().order_by('-id')
    serializer = UniversitySerializer(universities)
    return Response(serializer.data)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def dashboard_universities_info(request, pk):
    university = University.objects.get(id=pk)
    serializer = UniversitySerializer(university)
    return Response(serializer.data, status=HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_filtered_university_view(request):
    if request.GET.get('region'):
        university = University.objects.filter(region__icontains=request.GET.get('region'))
        serializers = UniversitySerializer(university, many=True)
    if request.GET.get('city'):
        university = University.objects.filter(city__icontains=request.GET.get('city'))
        serializers = UniversitySerializer(university, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def dashboard_filter_students_view(request):
    if request.GET.get('first_name'):
        student = Student.objects.filter(first_name__icontains=request.GET.get('first_name'))
        serializers = StudentSerializer(student, many=True)
    if request.GET.get('last_name'):
        student = Student.objects.filter(last_name__icontains=request.GET.get('first_name'))
        serializers = StudentSerializer(student, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def dashboard_student_details_view(request, pk):
    student = Student.objects.get(id=pk)
    serializers = StudentSerializer(student, many=False)
    return Response(serializers.data, status=HTTP_200_OK)












