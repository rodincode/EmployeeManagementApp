# Generated by Django 4.1.1 on 2022-09-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employees_verification_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
