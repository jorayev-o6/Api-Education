# Generated by Django 5.0.1 on 2024-02-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_student_languages_student_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
