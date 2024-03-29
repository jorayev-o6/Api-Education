# Generated by Django 5.0.1 on 2024-02-09 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_university_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, ' '), (2, 'accept'), (3, 'accept closed')], default=0)),
                ('info', models.TextField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.university')),
            ],
        ),
    ]
