# Generated by Django 5.0.1 on 2024-02-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_student_bio_alter_student_certificate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]