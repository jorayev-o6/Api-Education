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
    path('get-info-count/<int:pk>/', get_count_info_view, name='get-info-count'),
    path('get-students/<int:pk>/', get_students_view, name='get-students-view'),
    path('get-universities-answer/<int:pk>/', get_university_registered_view, name='get-universities-answer'),
    path('get-student-search/', students_filter_view, name='get-student-search'),
    path('get-university-single/<int:pk>/', get_university_single_view, name='get-university-single'),
    path('login/', dashboard_login_view, name='login'),
    path('get-dashboard-view/', get_dashboard_view, name='get-dashboard-view'),
    path('get-dashboard-universities-view/', get_universities_view, name='get-dashboard-universities'),
    path('get-dashboard-universities-details/', dashboard_universities_info, name='get-dashboard-universities-info'),
    path('get-filtered-universities-view/', get_filtered_university_view, name='get-filtered-universities'),
    path('get-filter-students-view/', dashboard_filter_students_view, name='get-filter-students-views'),
    path('get-dashboard-student-details/<int:pk>/', dashboard_student_details_view, name='student-details'),

]