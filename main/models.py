from django.db import models

# Create your models here.
from django.db import models


class Banner(models.Model):
    img = models.ImageField(upload_to='BannerIMG')
    title = models.CharField(max_length=255)
    mid_title = models.CharField(max_length=255)
    typ_education = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class About(models.Model):
    img = models.ImageField(upload_to='AboutIMG')
    quantity = models.IntegerField(default=0)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='FacultyIMG')

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    icon = models.ImageField(upload_to='AboutMeIMG')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Degree(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class UnivGallery(models.Model):
    img = models.ImageField(upload_to='UnivGalleryIMG')


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    img = models.ImageField(upload_to='UniversityIMG')
    banner = models.ImageField(upload_to='UniversityBanner')
    address = models.CharField(max_length=255)
    about = models.FileField(upload_to='UniversityIMG')
    rating = models.IntegerField()
    price = models.IntegerField()
    process = models.CharField(max_length=255)
    control = models.CharField(max_length=255)
    gallery = models.ManyToManyField(UnivGallery)
    motto = models.CharField(max_length=255)
    degree = models.ManyToManyField(Degree, null=True, blank=True)
    faculty = models.ManyToManyField(Faculty)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='StudentIMG')
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.CharField(max_length=255)
    passport = models.FileField(upload_to='StudentPassport')
    certificate = models.FileField(upload_to='StudentCertificate', null=True, blank=True)
    ielts = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=(
        (1, 'Man'),
        (2, 'Woman')
    ), default=1)
    status = models.IntegerField(choices=(
        (1, 'accept document'),
        (2, 'closed document')
    ))

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name


class StudentComment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class PhoneContact(models.Model):
    phone = models.CharField(max_length=25)
    telegram = models.BooleanField(default=False)


class SubmitUniversity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    passport = models.FileField(upload_to='RegisPast')
    certificate = models.FileField(upload_to='Register/Certificate')
    answer = models.CharField(max_length=255, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.IntegerField(choices=(
        (1, ' '),
        (2, 'accept'),
        (3, 'cancelled'),
    ), default=0)
    info = models.TextField()

    def __str__(self):
        return str(self.university)


class PersonalMeneger(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField()



