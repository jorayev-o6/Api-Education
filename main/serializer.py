from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Banner
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = About
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = University
        fields = '__all__'


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = AboutMe
        fields = '__all__'


class StudentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = StudentComment
        fields = '__all__'


class ContactPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = PhoneContact
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Student
        fields = '__all__'


class SubmitUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = SubmitUniversity
        fields = '__all__'


class PersonalManagerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = PersonalMeneger
        fields = '__all__'




