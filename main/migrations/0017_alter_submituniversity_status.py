# Generated by Django 5.0.1 on 2024-02-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submituniversity',
            name='status',
            field=models.IntegerField(choices=[(1, ' '), (2, 'accept'), (3, 'cancelled')], default=0),
        ),
    ]
