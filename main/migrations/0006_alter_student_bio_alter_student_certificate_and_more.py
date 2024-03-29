# Generated by Django 5.0.1 on 2024-02-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_university_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='StudentCertificate'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ielts',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]
