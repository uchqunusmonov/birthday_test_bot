# Generated by Django 5.0.2 on 2024-03-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_position_delete_feedback_employee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
