# Generated by Django 4.2.10 on 2024-03-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
