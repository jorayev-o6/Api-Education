from django.urls import path
from main.views import *


urlpatterns = [
    path('get-banner/', get_banner_view, name='get-banner'),
    path('search-university-faculty/', search_university_faculty_view, name='search-university-faculty'),
    path('get-about/', get_about_view, name='get-about'),
    path('get-popular-university/', get_popular_university, name='get-popular-university'),
    path('get-student-comments/', comment_students_view, name='get-student-comments'),
    path('search-university/', search_university_view, name='search-university'),
    path('university-details/<int:pk>/', university_details_view, name='university-details'),
    path('student-details/<int:pk>/', student_details_view, name='student-details'),
    path('request-join-university/', get_request_join_university_view, name='request-join-university'),
    path('request-join-university-details/<int:pk>/', get_request_join_details_view, name='request-join-details'),
    path('get-info-count/', get_count_info_view, name='get-info-count'),
]