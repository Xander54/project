# Generated by Django 4.2.5 on 2023-09-25 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlili', '0004_program_delete_choice_delete_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='task',
        ),
        migrations.RemoveField(
            model_name='program',
            name='time_line',
        ),
    ]
